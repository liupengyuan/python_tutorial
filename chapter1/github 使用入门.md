# github使用入门
- [x] 到github.com注册用户，假设用户名为：`yourname`
1. 网页版本github使用
- [x] 登陆
- 建立新项目。点`Repositories`-->`new`，在`Repository name`中键入项目名称，在`Description (optional)`中键入描述，勾选`Initialize this repository with a README`，然后点`Creat repository`，至此建立了一个新项目。
- 基本文件操作。在新项目中，点击`Creat new file`可以建立新文件，点击`Upload files`可以上传文件，点击`Find file`可以查找文件，点击`Clone or download`可以将整个项目下载到本地。
- 分支操作。点击`Branch:master`，在`Switch branches/tags`框内输入分支名后，点击`Creat branch`可以创建一个项目分支，在项目分支内进行修改后，点击`Compare & pull request`可以将分支与原来的项目主体(master)进行比较并请求合并(也就是请求项目管理员把你的分支拉到主项目中)，点击`Creat pull request`，然后点击`Merge pull request`，然后点击`Confirm merge`，然后填入评论，点击`comment`完成项目合并，最后点击`Delete branch`，至此已经完成了项目分支，分支修改，分支合并，以及删除分支。
- 关注项目与合作。回到github.com，在`Search GitHub`框中搜索项目名称或用户名如：`liupengyuan`，点击感兴趣的项目如：`iupengyuan.github.io`，点击右上角的`Fork`，可以拷贝该项目到自己的项目中。可以对项目进行修改更新以及`pull request`请求，但是需要原项目所有者如`liupengyuan`来进行`merge`。原项目也可能更改，这时候你会看到`This branch is xxx commits behind liupengyuan:master.`，此时你可以点击`pull request`，然后点击链接：`switching the base`，然后点击`Creat pull request`，然后在`Title`中起一个名字，比如`update`，然后点击`pull request`，最后点击`Merge pull request`，再点击`cofirm`，可以添加评论，点击`Comment`，至此，这个项目就得到了原项目的最新版本。
2. 通过git shell使用github（以后再写）
