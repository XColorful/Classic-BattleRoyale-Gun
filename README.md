# 经典大逃杀枪械包 | Classic BattleRoyale Gun

[中文](#经典大逃杀枪械包) | [English](#classic-battleroyale-gun)

# 经典大逃杀枪械包

💡[图文教程](https://github.com/XColorful/Classic-BattleRoyale-Gun/wiki)

本枪包为“拼好枪”性质的枪包，整合了各 TaCZ 枪械包中出现的《PUBG: BATTLEGROUNDS》枪械，并统一了子弹、配件等配置。
- 该仓库内容兼容 TaCZ 1.1.4 枪包格式
- 由于各枪包制作时并非在所有方面都有统一标准，可能会导致兼容性方面的一些问题
- 目前仅缺少3把枪械：DBS、R45、VSS

## 使用说明

### 下载前置枪包

由于各枪包资产都使用CC BY-NC-ND 4.0协议，本枪包不包含其他枪包的资产文件，请自行前往各枪包地址下载：
- [CIBR冲锋陷阵:重启 附属包](https://www.curseforge.com/minecraft/customization/tacz-charge-into-battle-reboot-pack)
- [经典重铸](https://www.curseforge.com/minecraft/customization/tacz-classics-reborn)
- [Cold War](https://www.curseforge.com/minecraft/customization/coldwarguns)
- [白鼠的“硝烟革命”枪械扩展](https://www.curseforge.com/minecraft/customization/tacz-gunpowder-revolution-great-war-gunpack)
- [IOWP 无限起源](https://www.curseforge.com/minecraft/customization/tacz-infinite-origin)
- [Suffuse GunSmoke Pack](https://www.curseforge.com/minecraft/customization/suffuse-gunsmoke)
- [TAC Zero 默认枪械包](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero)
- [全境封锁枪包](https://www.curseforge.com/minecraft/customization/tacz-the-division-gunpack)

### 安装枪包

将下载的枪包解压至 _./minecraft/tacz_ 文件夹下，分别按以下名称重命名解压后的文件夹：
- cibr_gunspack
- classic_rccrp
- cold_war
- gunpowder_revolution_gunpack
- infinite_origin
- suffuse_gunsmoke_pack
- tacz_default_gun
- the_division_pack

### 替换文件

将本枪包解压后的内容覆盖至 _./minecraft/tacz_ 文件夹下

> （可选）如果你只需要保留必要的PUBG枪械内容，将 _./minecraft/tacz/remove_unused_content_ 覆盖至 _./minecraft/tacz_ 下即可

### 脚本处理

运行枪包根目录的 `unify_constraint_in_animations.py` 和 `unify_geo_model_constraint_pos.py`，使大部分枪械开镜射击时不会贴脸

> （可选）运行 _./minecraft/tacz/classic_battleroyale_gun/data/cbrg/data/guns_ 下的几个脚本，输入路径为 _./minecraft/tacz_：
> - `basic_gun_data.py`
> - `closed_bolt_to_open_bolt.py`
> - `reset_armor_ignore.py`
> - `unify_crawl_recoil.py`

## 免责声明

本项目为粉丝个人创作，灵感来源于《PUBG: BATTLEGROUNDS》。所有知识产权，包括枪械的外观、纹理和音效，均归 Krafton, Inc. 所有。本项目为非盈利性质，与任何商业公司无关联。我尊重版权，并承诺如任何版权方提出移除要求，我将立即遵守。
- 代码：[GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
- 资产：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

# Classic BattleRoyale Gun

💡[Step-by-Step Guide](https://github.com/XColorful/Classic-BattleRoyale-Gun/wiki#English)

This is a "hodgepodge" gunpack that integrates and unifies various weapons from _PUBG: BATTLEGROUNDS_ found across different TaCZ gunpacks. It standardizes bullets, attachments, and other configurations.
- This repository is compatible with TaCZ 1.1.4 gunpack format.
- As the original gunpacks were not all created with uniform standards, there may be some compatibility issues.
- The following 3 weapons are currently missing: DBS, R45, and VSS.

## Instructions

### Download prerequisite gunpacks

This gunpack does not include any assets due to the CC BY-NC-ND 4.0 license of the original packs. You must download all prerequisite gunpacks from the links below:
- [CIBR GUN Pack](https://www.curseforge.com/minecraft/customization/tacz-charge-into-battle-reboot-pack)
- [Classics Reborn](https://www.curseforge.com/minecraft/customization/tacz-classics-reborn)
- [Cold War](https://www.curseforge.com/minecraft/customization/coldwarguns)
- [Hamster's GunpowderRevolution_gunpack](https://www.curseforge.com/minecraft/customization/tacz-gunpowder-revolution-great-war-gunpack)
- [IOWP Infinite Origin](https://www.curseforge.com/minecraft/customization/tacz-infinite-origin)
- [Suffuse GunSmoke Pack](https://www.curseforge.com/minecraft/customization/suffuse-gunsmoke)
- [TAC Zero Default Pack](https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero)
- [The Division park](https://www.curseforge.com/minecraft/customization/tacz-the-division-gunpack)

### Install the gunpacks

Extract each downloaded gunpack into your _./minecraft/tacz/_ folder and rename the resulting folders as follows:
- cibr_gunspack
- classic_rccrp
- cold_war
- gunpowder_revolution_gunpack
- infinite_origin
- suffuse_gunsmoke_pack
- tacz_default_gun
- the_division_pack

### Replace files

Extract the contents of this repository and copy them into your _./minecraft/tacz/_ folder, overwriting any existing files.
> (Optional) If you only want to keep the necessary PUBG weapons, overwrite _./minecraft/tacz/_ with the contents of _./minecraft/tacz/remove_unused_content/_ instead.

### Script processing

Run `unify_constraint_in_animations.py` and `unify_geo_model_constraint_pos.py` in the root directory of the gunpack to prevent most weapons from clipping through the camera when firing while aiming.

> (Optional) Run the following scripts under _./minecraft/tacz/classic_battleroyale_gun/data/cbrg/data/guns_, with the input path set to _./minecraft/tacz/_:
> - `basic_gun_data.py`
> - `closed_bolt_to_open_bolt.py`
> - `reset_armor_ignore.py`
> - `unify_crawl_recoil.py`

## Disclaimer

This is a fan-made project inspired by _PUBG: BATTLEGROUNDS_. All intellectual property, including weapon models, textures, and sounds, belongs to Krafton, Inc. This project is non-profit and not affiliated with any commercial company. I respect all copyrights and will comply with any request from the rights holders to remove this content.
- Code：[GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
- Assets：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)