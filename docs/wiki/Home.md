[English](#English)

## 使用说明

### 下载前置枪包

由于各枪包资产都使用CC BY-NC-ND 4.0协议，本枪包不包含其他枪包的资产文件，请自行前往各枪包地址下载：

| | |
|---|---|
|[CIBR冲锋陷阵:重启 附属包](https://www.curseforge.com/minecraft/customization/tacz-charge-into-battle-reboot-pack)|![cibr_gunspack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/cibr_gunspack%20download.png)|
|[经典重铸](https://www.curseforge.com/minecraft/customization/tacz-classics-reborn)|![classic_rccrp download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/classic_rccrp%20download.png)|
|[Cold War](https://www.curseforge.com/minecraft/customization/coldwarguns)|![cold_war download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/cold_war%20download.png)|
|[白鼠的“硝烟革命”枪械扩展](https://www.curseforge.com/minecraft/customization/tacz-gunpowder-revolution-great-war-gunpack)|![gunpowder_revolution_gunpack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/gunpowder_revolution_gunpack%20download.png)|
|[IOWP 无限起源](https://www.curseforge.com/minecraft/customization/tacz-infinite-origin)|![infinite_origin download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/infinite_origin%20download.png)|
|[Suffuse GunSmoke Pack](https://www.curseforge.com/minecraft/customization/suffuse-gunsmoke)|![suffuse_gunsmoke_pack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/suffuse_gunsmoke_pack%20download.png)|
|[TAC Zero 默认枪械包](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero)|![tacz_default_gun download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/tacz_default_gun%20download.png)|
|[全境封锁枪包](https://www.curseforge.com/minecraft/customization/tacz-the-division-gunpack)|![the_division_pack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/the_division_pack%20download.png)|

下载的文件应如图所示：
![Downloaded files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Downloaded%20files.png)

### 安装枪包

将下载的枪包解压至 _./minecraft/tacz_ 文件夹下，
> 全选，按住右键拖动至 _./minecraft/tacz_
> 
> ![Select all downloaded files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Select%20all%20downloaded%20files.png)
> 
> 松开右键，解压
> 
> ![Extract to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extract%20to%20tacz.png)
> 
> 解压后文件夹内容如下
> 
> ![Extracted files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extracted%20files.png)
> 
> 到 _./minecraft/tacz/tacz-1.20.1-1.1.7-hotfix/assets/tacz/custom_
> 
> ![tacz_default_gun in jar](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/tacz_default_gun%20in%20jar.png)
> 
> 将 _tacz_default_gun_ 文件夹剪切至 _./minecraft/tacz_
> 
> ![Cut tacz_default_gun to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Cut%20tacz_default_gun%20to%20tacz.png)
> 
> 再删除 _./minecraft/tacz/tacz-1.20.1-1.1.7-hotfix_
> 
> ![Delete files extracted from tacz jar](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Delete%20files%20extracted%20from%20tacz%20jar.png)

分别按以下名称重命名解压后的文件夹：
- cibr_gunspack
- classic_rccrp
- cold_war
- gunpowder_revolusion_gunpack
- infinite_origin
- suffuse_gunsmoke_pack
- tacz_default_gun
- the_division_pack
> ![Rename extracted folders](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Rename%20extracted%20folders.png)

### 替换文件

将本枪包解压后的内容覆盖至 _./minecraft/tacz_ 文件夹下
> ![Extract CBRG to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extract%20CBRG%20to%20tacz.png)
> 
> 替换文件
> 
> ![Confirm file replace](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Confirm%20file%20replace.png)
> 
> 解压后文件夹内容如下
> 
> ![Final extracted files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Final%20extracted%20files.png)

> （可选）如果你只需要保留必要的PUBG枪械内容，将 _./minecraft/tacz/remove_unused_content_ 覆盖至 _./minecraft/tacz_ 下即可
> 
> | | |
> |---|---|
> |![remove_unused_content](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/remove_unused_content.png)|![in remove_unused_content](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/in%20remove_unused_content.png)|
> 
> 全部替换
> 
> | | |
> |---|---|
> |![Replace the files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Replace%20the%20files.png)|![Replaced folders](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Replaced%20folders.png)|

### 脚本处理

> 下载安装 [Python](https://www.python.org/)
> 
> ![Download Python](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Download%20Python.png)

运行枪包根目录的 `unify_constraint_in_animations.py` 和 `unify_geo_model_constraint_pos.py`，使大部分枪械开镜射击时不会贴脸
> 运行完之后应产生两个日志文件，可删除
> ![Script log](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Script%20log.png)

> （可选）运行 _./minecraft/tacz/classic_battleroyale_gun/data/cbrg/data/guns_ 下的几个脚本，输入路径为 _./minecraft/tacz_：
> - `basic_gun_data.py`
> - `closed_bolt_to_open_bolt.py`
> - `reset_armor_ignore.py`
> - `unify_crawl_recoil.py`
> 
> ![Additonal scripts](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Additonal%20scripts.png)
> 
> 每个脚本都需要手动输入 _./minecraft/tacz_ 所在目录
> 
> ![Manually input tacz directory](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Manually%20input%20tacz%20directory.png)

## 免责声明

本项目为粉丝个人创作，灵感来源于《PUBG: BATTLEGROUNDS》。所有知识产权，包括枪械的外观、纹理和音效，均归 Krafton, Inc. 所有。本项目为非盈利性质，与任何商业公司无关联。我尊重版权，并承诺如任何版权方提出移除要求，我将立即遵守。
- 代码：[GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
- 资产：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

# English

## Instructions

### Download prerequisite gunpacks

This gunpack does not include any assets due to the CC BY-NC-ND 4.0 license of the original packs. You must download all prerequisite gunpacks from the links below:

| | |
|---|---|
|[CIBR GUN Pack](https://www.curseforge.com/minecraft/customization/tacz-charge-into-battle-reboot-pack)|![cibr_gunspack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/cibr_gunspack%20download.png)|
|[Classics Reborn](https://www.curseforge.com/minecraft/customization/tacz-classics-reborn)|![classic_rccrp download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/classic_rccrp%20download.png)|
|[Cold War](https://www.curseforge.com/minecraft/customization/coldwarguns)|![cold_war download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/cold_war%20download.png)|
|[Hamster's GunpowderRevolution_gunpack](https://www.curseforge.com/minecraft/customization/tacz-gunpowder-revolution-great-war-gunpack)|![gunpowder_revolution_gunpack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/gunpowder_revolution_gunpack%20download.png)|
|[IOWP Infinite Origin](https://www.curseforge.com/minecraft/customization/tacz-infinite-origin)|![infinite_origin download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/infinite_origin%20download.png)|
|[Suffuse GunSmoke Pack](https://www.curseforge.com/minecraft/customization/suffuse-gunsmoke)|![suffuse_gunsmoke_pack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/suffuse_gunsmoke_pack%20download.png)|
|[TAC Zero Default Pack](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero)|![tacz_default_gun download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/tacz_default_gun%20download.png)|
|[The Division park](https://www.curseforge.com/minecraft/customization/tacz-the-division-gunpack)|![the_division_pack download](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/the_division_pack%20download.png)|

The downloaded files should look like this:
![Downloaded files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Downloaded%20files.png)

### Install the gunpacks

Extract each downloaded gunpack into your _./minecraft/tacz/_ folder,
> Select all, right-click and drag to _./minecraft/tacz_
> 
> ![Select all downloaded files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Select%20all%20downloaded%20files.png)
> 
> Release right-click and select "Extract"
> 
> ![Extract to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extract%20to%20tacz.png)
> 
> The folder contents after extraction should look like this:
> 
> ![Extracted files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extracted%20files.png)
> 
> Go to _./minecraft/tacz/tacz-1.20.1-1.1.7-hotfix/assets/tacz/custom_
> 
> ![tacz_default_gun in jar](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/tacz_default_gun%20in%20jar.png)
> 
> Cut the _tacz_default_gun_ folder and paste it into _./minecraft/tacz_
> 
> ![Cut tacz_default_gun to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Cut%20tacz_default_gun%20to%20tacz.png)
> 
> Then delete the _./minecraft/tacz/tacz-1.20.1-1.1.7-hotfix_ folder
> 
> ![Delete files extracted from tacz jar](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Delete%20files%20extracted%20from%20tacz%20jar.png)

and rename the resulting folders as follows:
- cibr_gunspack
- classic_rccrp
- cold_war
- gunpowder_revolusion_gunpack
- infinite_origin
- suffuse_gunsmoke_pack
- tacz_default_gun
- the_division_pack
> ![Rename extracted folders](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Rename%20extracted%20folders.png)

### Replace files

Extract the contents of this repository and copy them into your _./minecraft/tacz/_ folder, overwriting any existing files.
> ![Extract CBRG to tacz](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Extract%20CBRG%20to%20tacz.png)
> 
> Replace files
> 
> ![Confirm file replace](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Confirm%20file%20replace.png)
> 
> The folder contents after extraction should look like this:
> 
> ![Final extracted files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Final%20extracted%20files.png)

> (Optional) If you only want to keep the necessary PUBG weapons, overwrite _./minecraft/tacz/_ with the contents of _./minecraft/tacz/remove_unused_content/_ instead.
> 
> | | |
> |---|---|
> |![remove_unused_content](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/remove_unused_content.png)|![in remove_unused_content](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/in%20remove_unused_content.png)|
> 
> Replace all
> 
> | | |
> |---|---|
> |![Replace the files](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Replace%20the%20files.png)|![Replaced folders](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Replaced%20folders.png)|

### Script processing

> Download and install [Python](https://www.python.org/)
> 
> ![Download Python](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Download%20Python.png)

Run `unify_constraint_in_animations.py` and `unify_geo_model_constraint_pos.py` in the root directory of the gunpack to prevent most weapons from clipping through the camera when firing while aiming.
> Two log files should be generated after running; these can be deleted.
> ![Script log](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Script%20log.png)

> (Optional) Run the following scripts under _./minecraft/tacz/classic_battleroyale_gun/data/cbrg/data/guns_, with the input path set to _./minecraft/tacz/_:
> - `basic_gun_data.py`
> - `closed_bolt_to_open_bolt.py`
> - `reset_armor_ignore.py`
> - `unify_crawl_recoil.py`
> 
> ![Additonal scripts](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Additonal%20scripts.png)
> 
> Each script requires you to manually input the directory where _./minecraft/tacz_ is located.
> 
> ![Manually input tacz directory](https://github.com/XColorful/Classic-BattleRoyale-Gun/HEAD/pic/Manually%20input%20tacz%20directory.png)

## Disclaimer

This is a fan-made project inspired by _PUBG: BATTLEGROUNDS_. All intellectual property, including weapon models, textures, and sounds, belongs to Krafton, Inc. This project is non-profit and not affiliated with any commercial company. I respect all copyrights and will comply with any request from the rights holders to remove this content.
- Code：[GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
- Assets：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)