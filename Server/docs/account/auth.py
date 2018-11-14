from docs import parameter

AUTH_POST = {
    'tags': ['Account'],
    'description': '회원가입',

    'parameters': {
        parameter('id', '아이디 (5자 이상 20자 이하)'),
        parameter('password', '비밀번호 (8자 이상 32자 이하)')
    },

    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': '액세스 토큰'
                }
            }
        },
        '204': {'description': '로그인 실패'}
    }
}
