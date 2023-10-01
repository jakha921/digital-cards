"""
This little script can generate a valid .vcf (vCard). It will ask you to fill
in some details and write the vcf-file.
"""

def main():
    print('Please enter contact details:')
    first_name   = input(' - First name       : ')
    last_name    = input(' - Last name        : ')
    email        = input(' - E-mail address   : ')
    company      = input(' - Company          : ')
    title        = input(' - Title            : ')
    phone_number = input(' - Phone number     : ')
    address      = input(' - Address          : ')
    okay()
    vcf_file = f'{first_name.lower()}.vcf'
    print(f'Will be writing vcard to: {vcf_file}')
    okay()
    vcard = make_vcard(first_name, last_name, company, title, phone_number, address, email)
    write_vcard(vcf_file, vcard)

def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        address,
        email):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])

def okay():
    okay = input('Okay [yes/no]? ')
    if okay in ['Yes', 'yes', 'YES', 'y', 'Y', 'ok']:
        return True
    else:
        print('Cancelled.')
        exit(1)

if __name__ == "__main__":
    main()