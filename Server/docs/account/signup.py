from docs import parameter

SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',

    'parameters': {
        parameter('id', '아이디 (5자 이상 20자 이하)'),
        parameter('password', '비밀번호 (8자 이상 32자 이하)'),
        parameter('email', '이메일')
    },

    'responses': {
        '201': {'description': '회원가입 성공'},
        '205': {'description': '회원가입 실패'}
    }
}