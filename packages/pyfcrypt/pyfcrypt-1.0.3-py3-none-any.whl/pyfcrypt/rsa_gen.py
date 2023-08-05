import sys
import click
import pathlib

#import fcrypt

# pyfcrypt klasör, digeri fcrypt dosya/modül.
# Bu sekilde yapmazsak pyinstallerda fcrypt modülü bulunamıyor.
# Hatasız python projeleri ici pyapp>pyapp->source files olmalı
#from pyfcrypt import fcrypt
#from pyfcrypt.fcrypt import *

import fcrypt


#from fcrypt import prompt_pass

#>
"""
import os, sys
try:
    print("Try 1")
    import fcrypt
    path = os.path.dirname(fcrypt.__file__)
    sys.path.insert(0, path)
    print("Try 1 File", path)
except:
    # using relative import
    print("Except 1")
    from . import fcrypt
    # discover path of the module and add it to the sys.path.
    path = os.path.dirname(fcrypt.__file__)
    sys.path.insert(0, path)
    print("adding path",path)

from fcrypt import prompt_pass
"""
#<


from Cryptodome.PublicKey import RSA


def quit():
    sys.exit()


"""

(CRETAE KEY PAIR - ENCRYPTED OR NOT)
# Creates a new public/private key pair and stores the private key in encrypted form
# Default Keylength is 2048 bits.
# Do not use file extension when creating the key pair.
# .public.pem , private.pem or private.pem.enc will be created automatically.

    (ENCRYPTED PRIVATE KEY)
    python rsa.py mykey --new-key (--enc Default) (--key-length 2048 Default)
    python rsa.py mykey --new-key --enc
    
    (UNENCRYPTED PRIVATE KEY)(NOT RECOMMENDED TO SAVE PRIVATE KEY AS PLAIN DATA!)
    python rsa.py mykey --new-key --no-enc

    (1024 BIT EXAMPLE)
    python rsa.py mykey --new-key --enc --key-length 1024
    

(EXPORT PUBLIC KEY FROM ENCRYPTED PRIVATE KEY)
# Decryptes private key(that was previosluy encrypted) on the fly, exports public key and save it to the disk.
# key without any extension or with exact file extension is accepted.
# system will automatically append  "private.pem.enc" extension to the key name that has no extensions. 

    python rsa.py mykey --dec-export
    python rsa.py mykey.private.pem.enc --dec-export-pub


(EXPORT PUBLIC KEY FROM UNENCRYPTED PRIVATE KEY)
# key without any extension or with exact file extension is accepted.
# system will automatically append  ".private.pem" extension to the key name that has no extensions. 

    python rsa.py mykey --export-pub
    python rsa.py mykey.private.pem --export-pub

"""


@click.command()
@click.argument('rsa_key_name')
@click.option('--new-key','-n', is_flag=True, help="Create new key pair")
@click.option('--enc/--no-enc','-e/-ne', is_flag=True, default=True, help="Encrypt private key or not")
@click.option('--dec-export-pub','-d', is_flag=True,  help="Decrypt private key and create public key file")
@click.option('--export-pub','-x', is_flag=True,  help="Export unencrypted private key and create public key file")
@click.option('--key-length', type=int, default=2048, help='Key length. Default value is 2048 bits.')
#@click.option('--pwd-visible', type=bool, default=False, help='Password visibility when typing.')
def rsa_main(rsa_key_name,new_key, enc, dec_export_pub, export_pub, key_length):

    #print("dec_export_pub",dec_export_pub)
    #print("new_key",new_key)
    #quit()

    if ((enc == True) and (new_key==True)):
        password = fcrypt.prompt_pass(ask_confirmation=True)
    elif  (dec_export_pub == True):
        password = fcrypt.prompt_pass(ask_confirmation=False)
    else:
        password = ""

    if (new_key==True):
        rsa_key = generate_key(rsa_key_name,key_length)

        # file name / may be virtual:
        f_name = rsa_key_name + ".private.pem"
        f_virtual_binary_data = rsa_key.export_key('PEM')

        if (enc==True):
            # We won't create private file on disk; instead feed the encrypt_file api with virtual_file flag
            click.echo("Private key encryption operation is started")
            fcrypt.encrypt_virtual_file(f_name, password, f_virtual_binary_data)
        else:
            # Private key is being saved to disk - with no encryption!
            with open(f_name, 'wb') as f:
                f.write(rsa_key.export_key('PEM'))

            f_absolute = pathlib.Path(f_name).absolute()
            click.echo("Private key ({0}) is created and saved at location {1}".format(f_name, f_absolute))
            click.echo(click.style("!!! Attention !!! Private key is saved to the disk with no encryption! You should consider protecting the private key file!", fg='bright_red'))

        # Save public key after private key is saved. (encrypt_virtual_file may generate abort condition)
        f_name = rsa_key_name + ".public.pem"
        with open(f_name, 'wb') as f:
            f.write(rsa_key.publickey().export_key('PEM'))

        f_absolute = pathlib.Path(f_name).absolute()
        click.echo("Public key ({0}) is created and saved at location {1}".format(f_name, f_absolute))

    elif (dec_export_pub==True) or (export_pub==True):

        if (dec_export_pub):
            default_extension = ".private.pem.enc"
        else:
            default_extension = ".private.pem"

        # Accept key name both with and without extension.
        f_extensions = pathlib.Path(rsa_key_name).suffixes
        if (len(f_extensions)==0):
            f_name = rsa_key_name + default_extension
        else:
            f_name = rsa_key_name

        # extensions are updated if default_extension is used above
        f_extensions = pathlib.Path(f_name).suffixes

        if (dec_export_pub):
            # Try decrypting private encrypted file
            plain_binary_data = fcrypt.decrypt_file(f_name,password,output_file=False)
        else:
            try:
                with open(f_name, "rb") as f:
                    plain_binary_data = f.read()
            except IOError as err:
                click.echo(click.style(f"File Error {err} {f_name}", fg='bright_red'))
                quit()

        rsa_key = RSA.import_key(plain_binary_data)

        # Remove all extensions
        f_name_wo_extension = f_name
        for i in range(len(f_extensions)):
            f_name_wo_extension = pathlib.Path(f_name_wo_extension).stem

        # Save public key
        f_name = f_name_wo_extension + ".public.pem"
        with open(f_name, 'wb') as f:
            f.write(rsa_key.publickey().export_key('PEM'))

        f_absolute = pathlib.Path(f_name).absolute()
        click.echo("Public key ({0}) is created and saved at location {1}".format(f_name, f_absolute))
    else:
        click.echo("Insufficient arguments. Try --help for arguments and options")



def generate_key(rsa_key_name,key_length):
    click.echo("Generating key ({0}) {1} bits".format(rsa_key_name,key_length))
    rsa_key = RSA.generate(key_length)

    return rsa_key

if __name__ == '__main__':
    rsa_main()



