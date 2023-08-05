import click
import configparser
import datetime
import json
import os
import sys
import pathlib
from base64 import b64encode
from base64 import b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Random import get_random_bytes
from Cryptodome.Hash import HMAC, SHA256


def quit():
    sys.exit()

"""
# Virtual Enviroment da terminalde click.style renkleri görünmüyor.
"""
is_key_visible = False

"""
python fcrypt.py myfile.zip --enc
python fcrypt.py myfile.zip.enc --dec


# --key-visible T 
# Reveals the generated keys and salt value for the single encryption operation.
# !!! Both the generated keys and salt value are different for each encryption operation/file. !!!
# !!! Thus it is not practical to save generated key and salt for each encryption operation.!!!
# For 3rd party decryption tool; salt can be obtained from the encrypted file headers(b64 encoded) and keys can be regenerated with
# PBkdf2 technique from the given password and salt value.

python fcrypt.py myfile.zip --enc --key-visible T

"""

@click.command()
@click.argument('file_name')
@click.option('--enc','-e', is_flag=True, help="Encrypt File. Ex: fcrypt file.xyz -e --pwd-visible Y --key-visible Y")
@click.option('--dec','-d',is_flag=True, help="Ex: fcrypt file.xyz.enc -d")
#@click.option('--pwd-visible', prompt='Password Visible?', type=bool, default=False, help='Password visibility when typing.')
@click.option('--key-visible', type=bool, default=False, help='Generated key visibility during encryption and decryption')
#@click.password_option(hide_input=False)
#@click.option('--password', prompt=True, confirmation_prompt=True,hide_input=True)
def fcrypt_main(file_name, enc, dec, key_visible):
    global is_key_visible
    is_key_visible = key_visible
    #click.echo('We received {0} as password.'.format(password))
    #click.confirm('Do you want to continue?',abort=True)

    #click.echo(click.style("Attention!", fg='red'))

    if ((enc==True) and (dec==True)) or ((enc==False) and (dec==False)):
        click.echo(click.style(f"Either select --enc(-e) or --dec(-d) flag", fg='yellow'))
        return

    if not os.path.isfile(file_name):
        click.echo(click.style("File not found", fg='bright_red'))
        return

    # if --pass-visible option is defined in command line; there wont be any question to ask as the user already entered.
    if (enc==True) and (dec==False):
        password = prompt_pass(ask_confirmation=True)
        encrypt_file(file_name,password)

    if (enc==False) and (dec==True):
        password = prompt_pass(ask_confirmation=False)
        decrypt_file(file_name,password)


def prompt_pass(ask_confirmation=False):

    pwd_visible = click.prompt('Show password when typing?', type=bool, default=False)
    password = click.prompt('Please enter the Password', hide_input=not(pwd_visible), confirmation_prompt=ask_confirmation,
                            type=str)
    pin = click.prompt('Please enter the Pin(Optional)(For distributed security)', hide_input=not(pwd_visible), confirmation_prompt=ask_confirmation,
                            type=str, default="")
    result = str(password).strip() + str(pin).strip()

    return result


# check if this password registered to the lookup
def lookup_pwd_hash(pwd_hash):

    f_name = "config.ini"
    section_name= "password-hashes"

    # Configparser - config.ini key'leri lowercase yapıyor ve base64 stringte sonundaki eşittir isareti sorun yaratıyor.
    # Bu nedenle config.ini dosyasında key'leri hes olarak tutacağız.
    pwd_hash_bytes = b64decode(pwd_hash)
    pwd_hash_hex_str = pwd_hash_bytes.hex()


    config = configparser.ConfigParser()
    config.read(f_name)

    if not config.has_section(section_name):  #.has_option(section, option)
        return False

    # if not pwd_hash in config[section_name]:
    if config.has_option(section_name,pwd_hash_hex_str):
        return True
    else:
        return False

    """
    for key in config[section_name]:
        print("Key",key,"pwd_hash_hex_str",pwd_hash_hex_str)
        if key==pwd_hash_hex_str:
            print("Found")
            return True
    """

    return False


def lookup_insert_pwd_hash(pwd_hash):

    # Configparser - config.ini key'leri lowercase yapıyor ve base64 stringte sonundaki eşittir isareti sorun yaratıyor.
    # Bu nedenle config.ini dosyasında key'leri hes olarak tutacağız.
    pwd_hash_bytes = b64decode(pwd_hash)
    pwd_hash_hex_str = pwd_hash_bytes.hex()

    f_name = "config.ini"
    section_name= "password-hashes"

    config = configparser.ConfigParser()
    config.read(f_name)
    #print("config",config.sections())

    if not config.has_section(section_name):
        config.add_section(section_name)

    #if not pwd_hash_hex_str in config[section_name]:
    if not config.has_option(section_name,pwd_hash_hex_str):
        config[section_name][pwd_hash_hex_str] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(f_name, 'w+') as configfile:
        config.write(configfile)



#f_binary_data type -> bytes()
def encrypt_virtual_file(f_full_path,password,f_binary_data):
    encrypt_file(f_full_path,password,f_binary_data, virtual_file=True, delete_original_file=False)


def encrypt_file(f_full_path,password, f_binary_data=bytes(), virtual_file = False,delete_original_file=False ):

    pwd_hash = generate_lookup_hash(password)
    if not (lookup_pwd_hash(pwd_hash)):
        # Inform user that there is no password hash is stored previosly. It might be first time or wrong password possibly from a typo.
        click.echo(click.style("Attention!",
                               fg='bright_red'))
        click.echo(click.style("There is no previous hash record found for this password. Make sure you dont have a typo when writing the passsword. Otherwise your file cannot be decrypted again", fg='bright_red'))
        click.echo(click.style("This is normal to have this warning if this is the first time usage of your password",
                               fg='bright_red'))
        click.confirm('Do you want to continue for encryption of the file?',abort=True)
        lookup_insert_pwd_hash(pwd_hash)



    # Single extension is removed. We need to use multiple extensions.
    #f_ext = pathlib.Path(f_full_path).suffix
    # We use all extensions . Single extension used above breaks the orginal file name i.e. private.pem files.
    f_extensions = pathlib.Path(f_full_path).suffixes
    f_ext ="".join(f_extensions)
    f_name = pathlib.Path(f_full_path).stem
    f_absolute = pathlib.Path(f_full_path).absolute()
    #print("f_ext",f_ext)
    #print("f_name", f_name)
    #print("f_absolute", f_absolute)

    if not virtual_file:
        #f_binary_data = bytes()
        try:
            with open(f_full_path, "rb") as f:
                f_binary_data = f.read()
        except IOError as err:
            click.echo(click.style(f"File Error {err}", fg='bright_red'))
            quit()
    else:
        # Use the file content passed into this function. f_binary_data
        if (len(f_binary_data)==0):
            click.echo(click.style("Invalid input", fg='bright_red'))
            quit()

    # Generate key from password and create random salt value.
    generated_key, pwd_salt = generate_key_from_password(password)

    # Keep "original file extension" and "salt" value(to create PBkdf2 key) in the header part as json format
    str_header_original_file_extension = "\"Original File Extension\":\"{0}\"".format(f_ext)
    str_header_salt = "\"Salt\":\"{0}\"".format(pwd_salt.hex())
    str_header = "{ " + str_header_original_file_extension +", " + str_header_salt + " }"
    header = str_header.encode()

    # Encrypt data, and create json file
    # C# AesGcm uyumlulugu icin nonce 12 byte olmalı.
    # Cryptodome kutuphanesi 16byte'a gore olusturuyor, nonce belirtilmezse.
    nonce = get_random_bytes(12)
    cipher = AES.new(generated_key,AES.MODE_GCM, nonce=nonce)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(f_binary_data)
    json_k = [ 'nonce', 'header', 'tag', 'ciphertext' ]
    json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, tag, ciphertext)]
    json_result = json.dumps(dict(zip(json_k, json_v)))

    # Save encrypted file(json formatted)
    f_encrypted_full_path = f_full_path + ".enc"
    with open(f_encrypted_full_path,"w") as f:
        f.write(json_result)

    f_enc_absolute = pathlib.Path(f_encrypted_full_path).absolute()
    if not virtual_file:
        click.echo(click.style(f"{f_full_path} is encrypted and saved as {f_encrypted_full_path} at location {f_enc_absolute}", fg='green'))
    else:
        click.echo(click.style(f"{f_full_path}(virtual file) is encrypted and saved as {f_encrypted_full_path} at location {f_enc_absolute}", fg='green'))

    # dont ask to delete, if delete original file is passed as True
    if not virtual_file:
        #Ask to delete original file if this is not a virtual file.
        if (delete_original_file):
            delete_file(f_full_path,f_absolute)
        else:
            # Ask if original file is deleted?
            if (click.confirm(f'Do you want to delete the original file? (unencrypted) {f_name}{f_ext}', default=False)):
                click.echo(f'Deleting File {f_full_path}')
                delete_file(f_full_path,f_absolute)
                quit()
            else:
                click.echo(click.style("Original file is not deleted", fg='yellow'))

def delete_file(f_full_path, f_absolute):
    try:
        os.remove(f_full_path)
        click.echo(click.style(f"File deleted at {f_absolute}", fg='green'))
    except IOError as err:
        click.echo(click.style(f"File Error {err}", fg='bright_red'))


def decrypt_file(f_encrypted_full_path,password, output_file=True):

    print("Decrytping file", f_encrypted_full_path)

    json_input = ""
    try:
        with open(f_encrypted_full_path, "r") as f:
            json_input = f.read()
    except IOError as err:
        click.echo(click.style(f"File Error {err}", fg='bright_red'))
        quit()


    b64 = json.loads(json_input)
    json_k = ['nonce', 'header', 'tag', 'ciphertext']
    jv = {k: b64decode(b64[k]) for k in json_k}


    # header includes another json data with key(s).
    # The first attempt for parsing(json.loads)above cannot resolve these keys as they were binary64 encoded.
    # We need to parse again after binary64 decoded

    header = json.loads(jv['header'])
    original_file_extension = header["Original File Extension"]
    print("Original File Extension",original_file_extension)

    # salt is required to regenerate the key from password.
    # It is expected to be stored in header key of .enc json file during encrypting
    # Salt is not required to be secret nut should be unique for best practices.
    pwd_salt_hex = header["Salt"]

    f_extensions = pathlib.Path(f_encrypted_full_path).suffixes
    f_dir = pathlib.Path(f_encrypted_full_path).parent #parents[0]) , parents[1] for previosu directory...and so on...
    f_absolute = pathlib.Path(f_encrypted_full_path).absolute()

    # Remove all extensions
    f_name_wo_extension = f_encrypted_full_path
    for i in range(len(f_extensions)):
        f_name_wo_extension = pathlib.Path(f_name_wo_extension).stem

    target_full_path_w_extension = str(f_dir)+ "\\" + f_name_wo_extension + original_file_extension

    generated_key, n = generate_key_from_password(password,pwd_salt_hex)

    try:
        cipher = AES.new(generated_key, AES.MODE_GCM, nonce=jv['nonce'])
        cipher.update(jv['header'])
        plain_data = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])

        # Binary calistigimiz icin .decode hata verir!
        #print("The message was: " + plaintext.decode())

        if (output_file):
            with open(target_full_path_w_extension, "wb") as f:
                f.write(plain_data)

            click.echo(f"({f_absolute})")
            click.echo(click.style(f"Decryption success. {target_full_path_w_extension} is created", fg='green'))

        return plain_data

    except (ValueError, KeyError) as err:
        click.echo(click.style(f"Decryption Error {err}", fg='bright_red'))
    except IOError  as err:
        click.echo(click.style(f"File Error {err}", fg='bright_red'))


# We create hash(hash) -> hmac(sha2) to store has in the lookup file
# to check if the password was previosly used(stored in lookup table) to prevent encryption with incorrect password rised from typo.
def generate_lookup_hash(password):
    sha2 = SHA256.new(password.encode("utf-8"))
    sha2_res_hex_str = sha2.hexdigest()
    hmac = HMAC.new(password.encode("utf-8"),bytes.fromhex(sha2_res_hex_str),digestmod=SHA256)
    hmac_res_hex_str = hmac.hexdigest()
    #print("hmac_res_hex_str",hmac_res_hex_str)
    hmac_base64 = b64encode(bytes.fromhex(hmac_res_hex_str))
    return hmac_base64.decode("utf-8")



# if pwd_salt_hex is provided, new salt will not be created. Possibly decrypting function calling is a salt is given
def generate_key_from_password(password, pwd_salt_hex="", key_length = int(256/8),iteration=1000000):

    # Salt is required to be unique for each user/password and can be stored in database in plain format
    # It does not reveal the key provided thatmost secure salt algorithms are used
    # This is to prevent users having same password

    if len(pwd_salt_hex)==0:
        pwd_salt_bytes = get_random_bytes(32)
    else:
        pwd_salt_bytes = bytes.fromhex(pwd_salt_hex)


    # We abonden here to generate salt from password; as some day hash algorithm may be broken and reveal the password.
    # Also we are trying to go with best practices and avoid wiriting our own cryptography system which is stritly not recommended!
    # The following code is placed here and commented just for API usage example.
    """
    # First create salt from password that is required for PBKDF2. So that we dont need to store salt value.
    # Salt value does need to be secured. It does not compromise actual password provided that modern hash algortims are used.
    # (i.e. MD5 cannot ve used!)
    #sha3_message_for_hmac = SHA3_512.new()
    #sha3_message_for_hmac.update((psw_salt_prefix+password +psw_salt_suffix).encode("utf-8"))
    #sha3_message_for_hmac_res = sha3_message_for_hmac.hexdigest()
    #print(sha3_message_for_hmac_res)

    #hmac_salt_for_pbkdf2 = HMAC.new((psw_salt_prefix+password + psw_salt_suffix).encode(), digestmod=SHA256)
    #hmac_salt_for_pbkdf2.update(bytes.fromhex(sha3_message_for_hmac_res))
    #hmac_salt_for_pbkdf2_res = hmac_salt_for_pbkdf2.hexdigest()
    #print(hmac_salt_for_pbkdf2_res)
    """

    # Create 32Byte x 4 Key. This later can be shortened or extended - Keys will be produced same order.
    # i.e. 32 x 4 and 32 x 1 will produce same key for the first 32 bytes.
    # iteration count delays the function to prevent brute-force attacks
    #keys= PBKDF2(password, bytes.fromhex(hmac_salt_for_pbkdf2_res), key_length, iteration)
    keys= PBKDF2(password,pwd_salt_bytes , key_length, iteration)
    if (is_key_visible):
        click.echo(click.style(f"Generated Key {keys.hex()}", fg='yellow'))
        click.echo(click.style(f"Generated Salt {pwd_salt_bytes.hex()}", fg='yellow'))

    return keys, pwd_salt_bytes


if __name__ == '__main__':
    password=""
    fcrypt_main()


