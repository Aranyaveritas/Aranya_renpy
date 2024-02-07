define a = Character("玥无")



label start:
    play music "./music/music.mp3"
    "旁白的测试短句"

    play sound "./music/start.mp3"
    a "已经开始游戏"
    stop sound
    
    play sound"./music/hello-myfirend.mp3"
    a "你好啊我的朋友"
    stop sound 
    
    play sound "./music/duohangceshi.mp3"
    a """
    尝试多行语句测试
    第一句话
    第二句话
    第三句话
    """
    stop sound

    play sound "./music/gameover.mp3"
    "接下来游戏要结束了"


 
return

                      