# github使用入门
- [x] 到github.com注册用户，假设用户名为：`yourname`
1. 网页版本github使用
- [x] 登陆
- 建立新项目。点`Repositories`-->`new`，在`Repository name`中键入项目名称，在`Description (optional)`中键入描述，勾选`Initialize this repository with a README`，然后点`Creat repository`，至此建立了一个新项目。
- 基本文件操作。在新项目中，点击`Creat new file`可以建立新文件，点击`Upload files`可以上传文件，点击`Find file`可以查找文件，点击`Clone or download`可以将整个项目下载到本地。
- 分支操作。点击`Branch:master`，在`Switch branches/tags`框内输入分支名后，点击`Creat branch`可以创建一个项目分支，在项目分支内进行修改后，点击`Compare & pull request`可以将分支与原来的项目主体(master)进行比较并请求合并(也就是请求项目管理员把你的分支拉到主项目中)，点击`Creat pull request`，然后点击`Merge pull request`，然后点击`Confirm merge`，然后填入评论，点击`comment`完成项目合并，最后点击`Delete branch`，至此已经完成了项目分支，分支修改，分支合并，以及删除分支。
- 关注项目与合作。回到github.com，在`Search GitHub`框中搜索项目名称或用户名如：`liupengyuan`，点击感兴趣的项目如：`iupengyuan.github.io`，点击右上角的`Fork`，可以拷贝该项目到自己的项目中，可以顺便点一下`Star`，为项目加星。这时，就将iupengyuan.github.io克隆到你自己的github仓库中了，且仓库名称为：yourname/iupengyuan.github.io，然后可以对项目进行修改更新，或者上传文件。如果想将你自己在自己仓库`yourname/iupengyuan.github.io`中的更改合并到原作者的项目仓库`liupengyuan/iupengyuan.github.io`，则需要发起`pull request`请求。当然，需要等待原项目所有者如`liupengyuan`同意`merge`你的更改。

 - 得到原项目最新版本。当你打开`fork`到本地的项目如`yourname/iupengyuan.github.io`，如看到看到类似`This branch is xxx commits behind liupengyuan:master.`或`liupengyuan committed on GitHub  Merge pull request #xxx from yyyyyyyyy`的信息，说明原项目有更新。此时你可以点击`pull request`，进入`Comparing changes`页面，然后点击链接：`compare across forks`，然后将`base fork`设为自己本地仓库如`yourname/iupengyuan.github.io`，将`head fork`设为原作者项目仓库如`liupengyuan/iupengyuan.github.io`，然后点击`creat new pull request`，在框中输入更新信息，并点击`creat pull request`(此时等于是原项目`liupengyuan/iupengyuan.github.io`[`head fork`]向你的仓库`yourname/iupengyuan.github.io`[`base fork`]进行`pull request`请求)。拉到页面底部，点击`Merge pull request`，再点击`cofirm`，至此，这个项目就得到了原项目的最新版本。

2. 通过git shell使用github（以后再写）
