# 公众号配置
# 公众号appId
app_id = "wx6e6c1863313f417c"
# 公众号appSecret
app_secret = "5f43ff5194283a5d132923e50c51d750"
# 模板消息id
# 每日消息
template_id1 = "HwqGU-uZrsripDlruIeLDY_jSd7DeH9LMiPtYVc7kh0"
# 课程消息,上课提醒
template_id2 = "_iElWpylf6NZqOPOQNTROp99CIobxOT9ElY9l09Ke-s"
# 晚安心语
template_id3 = "j5pbhBtkwCNqa8mQp-qd-kCnlH6wV8FAGfDLhEUCiLI"
# 接收公众号消息的微信号
# 这是openid
user = ["odVvL52K0Tcl5rVQ-Ct0ajbCAVj4"]


# 信息配置
# 所在省份
province = "四川"
# 所在城市
city = "绵阳"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2022-9-9"
# 在一起的日子，格式同上------------计时器
love_date = "2001-12-1"
# 天行数据晚安心语 key
good_Night_Key = "4082bfd944c******************"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2022
month = 8
day = 29
# 每日推送时间
post_Time = "19:20:00"
# 每节课提醒时间（有课才会提醒）, 时:分:秒  的形式, 字符串, 根据个人需要设置几次
time_table = ["07:40:00", "09:40:00", "13:40:00", "15:40:00", "18:40:00"]
# 课程时间
course_Time = ["8:00--9:45", "10:00--11:45", "14:00--15:45", "16:00--17:45", "19:00--20:45"]
# 晚安心语及第二天课程推送时间
good_Night_Time = "22:55:00"
# 课程表 "1"代表第一周，依次类推，根据个人实际课表添加，有几周就添加几周,
# 每一行代表一天, 例如  ['', '编译原理', '', '数据库原理及应用', '数据分析原理', '']  代表周一
classes = \
    {
        "1": [
            ['', '编译原理', '', '数据库原理及应用', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '', ''],
            ['', '计算机网络', '', '数据挖掘技术', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "2": [
            ['', '', '编译原理', '', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '数据挖掘技术', '数据挖掘技术'],
            ['', '计算机网络', '', '数据挖掘技术6', '', ''],
            ['', '', '', '', '数据库原理及应用', ''],
            ['', '', '', '', '', '']
        ],
        "3": [
            ['', '编译原理', '', '数据库原理及应用', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '数据挖掘实验', '数据挖掘实验'],
            ['', '计算机网络', '', '数据挖掘技术', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "4": [
            ['', '编译原理', '', '数据库原理及应用', '数据分析原理', ''],
            ['数据挖掘技术', '', '乒羽俱乐部3', '', '数据可视化', ''],
            ['计算机网络', '', '编译原理', '数据库原理及应用', '', ''],
            ['', '', '', '', '数据挖掘实验', '数据挖掘实验'],
            ['', '计算机网络', '', '数据挖掘技术', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
    }

# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
