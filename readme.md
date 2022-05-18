# AnyBlog: Turn your directory tree into a blog website anywhere you want!

## What's AnyBlog

本项目致力于创建一个命令行工具，可以在任何目录，用一句命令启动一个服务，

服务可以浏览该目录下的所有markdown笔记，类似一个文件资源浏览器。

## How does it work

- 用`markdown2`库将`md`文件转为html
- 用`Jinja2`将html段插入模板
- 用`FastAPI`搭建服务
