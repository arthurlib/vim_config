"""
"curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
"使用以下命令检查状态 :PlugStatus
"输入下面的命令，然后按回车键安装之前在配置文件中声明的插件:PlugInstall
"更新插件:PlugUpdate
"更新插件后，按下 d 查看更改。或者，你可以之后输入 :PlugDiff 有时，更新的插件可能有新的 bug 或无法正常工作。
"要解决这个问题，你可以简单地回滚有问题的插件。输入 :PlugDiff 命令，然后按回车键查看上次 :PlugUpdate的更改，并在每个段落上按 X 将每个插件回滚到更新前的前一个状态
"删除插件:PlugClean
"升级vim-plug本身，请输入 :PlugUpgrade
"

"""
import os
import subprocess
import sys

base_path = os.path.dirname(os.path.realpath(sys.argv[0]))


def intall_plug_manager():
    cmd = "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
    subprocess.run(cmd, shell=True)


def gen_vimrc():
    map_dir = os.path.join(base_path, "map")
    nnoremap_dir = os.path.join(base_path, "nnoremap")
    setting_dir = os.path.join(base_path, "setting")

    def read_file(dir):
        context = []
        for file in [os.path.join(dir, i) for i in os.listdir(dir)]:
            with open(file) as f:
                context.append(f.read())
        return "\n".join(context)

    # print(read_file(map_dir))
    # print(read_file(nnoremap_dir))
    # print(read_file(setting_dir))
    result = "\n".join([read_file(map_dir), read_file(nnoremap_dir), read_file(setting_dir)])
    return result


def gen_plugs():
    from plugs import plug
    result = """
call plug#begin('~/.vim/plugged')

{plugs}

call plug#end()

{plugs_setting}
    """
    plugs = []
    plugs_setting = []

    plugs_dir = os.path.join(base_path, "plugs")
    print(plugs_dir)
    for plug in plug.plugs:
        if plug['status']:
            if plug.get('cmd', ''):
                print(plug['cmd'])
                # subprocess.run(plug['cmd'], shell=True)
            if plug.get('name', ''):
                plugs.append("Plug '%s'" % plug['name'])
            if plug.get('file', ''):
                plugs_setting.append(open(os.path.join(plugs_dir, plug['file'])).read() + '\n')
    result = result.format(plugs='\n'.join(plugs), plugs_setting='\n'.join(plugs_setting))
    # print(result)
    return result


def main():
    a = gen_plugs()
    b = gen_vimrc()
    r = a + '\n' + b
    with open('vimrc', 'w') as f:
        f.write(r)


if __name__ == "__main__":
    main()
