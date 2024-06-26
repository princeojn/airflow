def get_sftp():
    print('sftp 작업을 시작합니다')

def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')

def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    email = kwargs.get('email') or ''
    phone = kwargs.get('phone') or ''
    if email:
        print(email)
    if phone:
        print(phone)