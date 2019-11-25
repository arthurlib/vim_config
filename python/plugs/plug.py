plugs = [
    {
        'status': 1,
        'name': 'Chiel92/vim-autoformat',  # 代码格式化工具
        'file': 'vim-autoformat',
        'cmd': "pip3 install autopep8"
    },
    {
        'status': 1,
        'name': 'https://github.com/scrooloose/nerdtree',  # 文件浏览窗口
        'file': 'nerdtree',
        'cmd': ""
    },
    {
        'status': 1,
        'name': 'kien/rainbow_parentheses.vim',# 不同颜色区分括号匹配
        'file': 'rainbow_parentheses',
        'cmd': ""
    },
    {
        'status': 1,
        'name': 'https://github.com/bling/vim-airline',# 加强版的状态栏
        'file': '',
        'cmd': ""
    },
    {
        'status': 0,
        'name': 'w0rp/ale',# 代码自动检查,确保你的vim版本不低于8.0
        'file': 'ale',
        'cmd': "pip3 install flake8"
    },
    {
        'status': 1,
        'name': 'scrooloose/syntastic',# 代码自动检查
        'file': 'syntastic',
        'cmd': "pip3 install flake8"
    },
    {
        'status': 1,
        'name': 'https://github.com/ycm-core/YouCompleteMe',
        'file': 'YouCompleteMe',# 代码提示
        'cmd': ""
    },
]
