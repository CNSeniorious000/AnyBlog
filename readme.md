# AnyBlog: Turn your directory tree into a blog website anywhere you want!

本项目借鉴本人在GitLab上维护的项目[assets](https://jihulab.com/CNSeniorious000/assets)

## What's AnyBlog

本项目致力于创建一个命令行工具，可以在任何目录，用一句命令启动一个服务，

服务可以浏览该目录下的所有markdown笔记，类似一个文件资源浏览器。

## features

- 持久化统计访问量
- 方便好用的模板（比如长图）

## How does it work

- 用`markdown2`库将`md`文件转为html
- 用`Jinja2`将html段插入模板
- 用`FastAPI`搭建服务
- 最新进展都在[assets](https://jihulab.com/CNSeniorious000/assets)项目中
