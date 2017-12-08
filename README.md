ishadowsokcs网站目前已无法打开，源码只供学习使用

---

自动获取并配置 ishadowsocks 提供的3个免费的shadowsocks账号

因为它每6个小时都会更改密码 所以闲来无事便写了这个脚本.

如果出现长时间无响应，则有可能你的网络无法访问iss的网站

---

### 使用步骤：

1. 首先克隆到本地:

  `git clone https://github.com/Tallone/ishadowsocks.git`

2. 在你的虚拟环境中执行:
  
  `pip install -r requirements.txt`

3. 将`config.json`中`gui-config-path`的值改为你shadowsocks自己生成的文件`gui-config.json`的路径.

4. 运行，推荐自己写个批处理文件，每次就不用麻烦的切换环境再执行了。
5. 启动ss, 就可以看到已经配置好的3个服务器了
