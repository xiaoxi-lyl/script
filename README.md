# script
## 南京工业职业技术大学校园网登录（pc端）

该程序是使用python的chrome webdriver和selenium实现的，然后使用pyinstaller在虚拟环境下打包生成的exe文件，然后放入windows的开机自启任务中，即可实现自动登录


## 虚拟环境打包步骤：

安装参考：[pyinstaller虚拟环境打包](https://www.jianshu.com/p/2656fbc01c54)

上述环境安装完成后，可以直接使用如下命令：```pyinstaller -F -w -p "虚拟环境路径" 文件名称``` 即可完成文件打包，然后设置为windowss开机自启即可。

PS：虚拟环境打包生成的exe文件很小，约为6MB

selenium和webdriver没安装要自行安装，自行百度即可

暂未解决：开机自启会有个win的终端运行两秒钟，但在打包时已经将命令设置为不显示终端，猜测可能是webdriver的问题，但是无伤大雅。有强迫症的同学可以自行解决
