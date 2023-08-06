# Taara

Android ANR自动分析工具

## 安装

```
pip instal taara
```

## 基本使用

```
$ taara --help

-------------------------------------------------------
                  Taara v0.1.6

Thanks for using Taara! Now, the doc is available on:
        https://code.byted.org/hproject/taara

                   Have Fun!
-------------------------------------------------------
usage: taara [-h] [-m MAPPING_PATH] [anr_file_path [anr_file_path ...]]

Analysis Android ANR automatically

positional arguments:
  anr_file_path         the file of /data/anr/traces.txt

optional arguments:
  -h, --help            show this help message and exit
  -m MAPPING_PATH, --mapping_path MAPPING_PATH
                        the path of mapping to retrace
```

## 案例

![](https://code.byted.org/hproject/taara/raw/master/arts/dead_lock_sample.png?inline=false)
