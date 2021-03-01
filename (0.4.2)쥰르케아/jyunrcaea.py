print("로딩중입니닷");
version = "0.4.2";
print("(로딩이 좀 오래걸린다면 엔터키를 연타해보세요!)");
print("(그래도 안되면 당신의 컴퓨터 성능 딸린겁니다...)");
print("------------------------------------");
#대충 pygame 모듈 불러오기
import pygame;
import os;
import os.path;
import time
from pygame.image import load
from pygame.mixer import Sound;
print("-------------------------------------");
print("만든놈? 쥰니");
print("버전:",version);
print("홈페이지요? http://pygame.614.kro.kr");
print("뭘로 만들었냐고요? Visual Studio Code");
print("모듈이요? pygame");
print("로딩중임 이예에예예예예에에에에에");
print("------------------------------------");
running = True; #실행
#기본설정
pygame.init(); #모듈 초기화
pygame.display.set_caption("JYUNRCAEA"); #창 제목
#데이터 불러오기
background = pygame.image.load("data/back.png"); #배경
butten = pygame.image.load("data/butten.png"); #버튼
setbutten = pygame.image.load("data/setbutten.png"); #선택버튼
set_text = pygame.image.load("data/set.png"); #선택바
fpsfont = pygame.font.Font("data/font.ttf", 40); #fps 표시에 알맞는 크기의 폰트
mainfont = pygame.font.Font("data/font.ttf", 75); #기본 크기의 폰트
intro = pygame.image.load("data/intro.png"); #인트로
pygame.mixer.music.load("music/knight_rider.mp3"); #메인화면 노래
fpsfpsfont = pygame.font.Font("data/font.ttf", 30); #작은 글자 표시에 알맞는 크기의 폰트
localdisk_c = pygame.image.load("data/localdisk.c.png"); #어.. c드라이브?
localdisk_d = pygame.image.load("data/localdisk.d.png"); #d드라이브?
disk_set = pygame.image.load("data/localdisk.set.png"); #디스크 선택바
backnote = pygame.image.load("data/backnote.png"); #노트 
setbacknote = pygame.image.load("data/set_backnote.png"); #선택된 노트
text_background = pygame.image.load("data/textbackground.png"); #뭐였지
jyunrcaea_icon = pygame.image.load("data/jyunrcaea_icon.png"); #아이콘
#아이콘 설정
pygame.display.set_icon(jyunrcaea_icon);
#음악 임시변수 (배열쓰기엔 [] 누르기 귀찮음)
music1 = 0;
music2 = 0;
music3 = 0;
music4 = 0;
music5 = 0;
music6 = 0;
music7 = 0;
music8 = 0;
music9 = 0;
#인트로 임시변수 (배열쓰기엔 [] 누르기 귀찮음)
intro1 = 0;
intro2 = 0;
intro3 = 0;
intro4 = 0;
intro5 = 0;
intro6 = 0;
intro7 = 0;
intro8 = 0;
intro9 = 0;
#최적화를 위한 임시변수
render = [0,0,0,0,0,0,0,0,0];
#변수들
notelist = [];
musiclist = [0 , 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]; #노래들
composer = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]; #작곡가들
varvar = 1; #선택 임시변수
key = False; #왼손 중지
key2 = False; #왼손 검지
key3 = False; #오른손 검지
key4 = False; #오른손 중지
key0 = False; #왼손 약지
key5 = False; #오른손 약지
up8 = False; #위
down2 = False; #아레
left4 = False; #왼쪽
right6 = False; #오른쪽
space = False; #그냥 스페이스바...
stop = False; #멈춰랏
stopkey = True; #멈춤키 반복방지 
gamepage = 0; #장면
set_set = 0; #선택위치
set_y = 90; #뭐였지
log = [0 ,0 ,0]; #기록
setting = [False , True , True , False , False]; #프레임 표시, ESC키 강제종료, 배경음악 재생, 미정 ,콘솔 로그 표시
fpstick = 60; #프레임 제한
fpsfps = [1600 , 900 , 0 , 0 , 0 , 0]; #5초내 초당프레임 측정, 처음 창 길이 임시변수로 사용
playsound = 0; #노래선택
playtext = ""; #글자표시
#변수 2
tpfh = -90;
starttime = 0;
playtime = 0;
r_time = 0; #시간
s_time = pygame.time.get_ticks(); #시작시간
clock = pygame.time.Clock(); #초당프레임 제한 클락
#함수
def notebutten():
    global key, key2, key3 , key4, tpfh;
    if key:
        screen.blit(setbacknote, (540, tpfh));
    else:
        screen.blit(backnote, (540, tpfh));
    if key2:
        screen.blit(setbacknote, (670, tpfh));
    else:
        screen.blit(backnote, (670, tpfh));
    if key3:
        screen.blit(setbacknote, (800, tpfh));
    else:
        screen.blit(backnote, (800, tpfh));
    if key4:
        screen.blit(setbacknote, (930, tpfh));
    else:
        screen.blit(backnote, (930, tpfh));
def gotoplaying():
    global space, gamepage, playsound;
    if space:
        space = False;
        gamepage = 19;
        playsound = 10;
#깊고 어두운 설명
print("로딩 완료!")
print("--------------------------------------");
print("1600x900 크기로 실행됩니다.");
print("60프레임(fps) 제한으로 실행됩니다.(변경 가능)")
screen = pygame.display.set_mode((fpsfps[0],fpsfps[1]));#창 길이 맞추기
fpsfps[0] = 0; fpsfps[1] = 0;
print("-----------------조작법---------------");
print("esc키로 종료(설정에서 끌수 있음)");
print("왼쪽 화살표키로 왼쪽이동");
print("오른쪽 화실표키로 오른쪽 이동");
print("위쪽 화살표키로 위쪽 이동");
print("아레쪽 화살표키로 아레쪽 이동");
print("d키 f키 j키 k키로 노트 및 롱노트 터치");
print("s키 및 l키로 모서리 노트 및 모서리 롱노트 터치");
print("--------------------------------------");
pygame.mixer.music.play(-1); #배경음악 재생
pygame.mixer.music.set_volume(0.5);
print("게임시작!");
print("아직 미완성 작입니다 ㅎㅎ;;");
#파일 확인
screen.blit(background, (0,0));
m_t = mainfont.render("파일을 확인하는 중입니다...", True , (255,255,255));
set_set = m_t.get_rect().size;
set_set = set_set[0] / 2
screen.blit(m_t, (set_set , 410));
pygame.display.update();
#게임시작
while running:
    if fpstick != 0:
        tick = clock.tick(fpstick); #프레임 
    #키 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.KEYDOWN: #키를 눌렀을떄 이벤트
            if event.key == pygame.K_ESCAPE: #esc키 눌렀을때
                if setting[1]: #ESC키 강제종료 설정
                    running = False;
            if event.key == pygame.K_q:
                if stopkey:
                    stopkey = False;
                    if stop:
                        stop = False;
                    else:
                        stop = True;
            if event.key == pygame.K_d: #d키 눌렀을떄
                key = True; log[1] += 1;
            if event.key == pygame.K_f: #f키 눌렀을떄
                key2 = True; log[1] += 1;
            if event.key == pygame.K_j: #j키 눌렀을때
                key3 = True; log[1] += 1;
            if event.key == pygame.K_k: #k키 눌렀을때
                key4 = True; log[1] += 1;
            if event.key == pygame.K_s: #s키 눌렀을때
                key0 = True; log[1] += 1;
            if event.key == pygame.K_l: #l키 눌렀을떄
                key5 = True; log[1] += 1;
            if event.key == pygame.K_UP: #위키 눌렀을때
                up8 = True; log[1] += 1;
            if event.key == pygame.K_LEFT: #왼쪽키 눌렀을떄
                left4 = True; log[1] += 1;
            if event.key == pygame.K_DOWN: #아레키 눌렀을때ㄷ
                down2 = True; log[1] += 1;
            if event.key == pygame.K_RIGHT: #오른쪽 키 눌렀을때
                right6 = True; log[1] += 1;
            if event.key == pygame.K_SPACE: #스페이스키를 눌렀을떄
                space = True; log[1] += 1;
            if event.key == pygame.K_TAB: #로그
                print("------");
                print("d키",key);
                print("f키",key2)
                print("j키",key3);
                print("k키",key4);
                print("------");
                print("s키",key0);
                print("l키",key5);
                print("------");
                print("스페이스키",space);
                print("경과시간",r_time);
                print("프레임",fpsfps);
            #키를 눌렀을때 이벤트 끝
        #키를 땟을때 이벤트
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: #d키 뗏을때
                key = False;
            if event.key == pygame.K_f: #f키 뗏을때
                key2 = False;
            if event.key == pygame.K_j: #j키 뗏을떄
                key3 = False;
            if event.key == pygame.K_k: #k키 똇을때
                key4 = False;
            if event.key == pygame.K_s: #s키 뗏을때
                key0 = False;
            if event.key == pygame.K_l: #l키 뗏을때
                key5 = False;
            if event.key == pygame.K_UP: #위키 뗏을떄
                up8 = False;
            if event.key == pygame.K_LEFT: #왼쪽키 똇을떄
                left4 = False;
            if event.key == pygame.K_DOWN: #아레키 똇을떄
                down2 = False;
            if event.key == pygame.K_RIGHT: #오른쪽키 똇을때
                right6 = False;
            if event.key == pygame.K_SPACE: #스페이스키를 뗏을때
                space = False;
        #키를 똇을떄 이벤트 끝
    #키 이벤트 끝
    #본격적으로 게임시작
    if (gamepage == 0): #처음 게임 시작할때
        screen.blit(background , (0, 0)); #배경화면 그리기
        screen.blit(intro , (0, 0));    
        if (space == True):
            space = False;
            set_set = 0; 
            gamepage = 1; #메인화면으로 이동
            set_y = 0; #이거 뭐였더라
            intro = pygame.image.load("data/mainintro.png") #메인화면에 띄울 사진 로드
        if r_time > 120:
            running = False;
    elif (gamepage == 1):
        screen.blit(background, (0, 0));
        screen.blit(intro, (-10 , 0))
        if down2 and not up8: #아레키를 눌렀을떄
            down2 = False;
            if set_set < 3: #선택바가 맨 아레는 아닐때
                set_set += 1; #값을 올려 내리기
            else: #선택바가 맨 아레일떄
                set_set = 0; #값을 싹 내려 맨위로 올리기
        elif up8 and not down2: #위키를 눌렀을떄
            up8 = False;
            if set_set > 0: #선택바가 맨 위는 아닐떄
                set_set -= 1; #값을 내려 올리기
            else: #선택바가 맨 위일때
                set_set = 3; #값을 싹 올려 맨 아레로 내리기
        if set_set == 0: #게임시작
            if space:
                space = False;
                set_set = 0;
                gamepage = 6;
            screen.blit(set_text, (0, 295));
        if set_set == 1:
            if space:
                space = False;
                set_set = 0;
                gamepage = 30;
                intro1 = mainfont.render("아직 미완성입니다, 3초후 돌아갑니다.", True, (255,255,255));
                intro2 = mainfont.render("(스페이스바를 눌러 돌아갈수 있습니다.)", True, (255,255,255));
                varvar = r_time + 3;
            screen.blit(set_text, (0, 395))
        if set_set == 2: #설정
            if space:
                space = False;
                set_set = 0;
                gamepage = 2;
                music1 = mainfont.render("초당 프레임 제한", True , (255,255,255));
                music2 = mainfont.render("기록 및 정보",True,(255,255,255));
                music3 = mainfont.render("설정 나가기", True ,(255 , 255, 255));
                music4 = mainfont.render("설정", True , (255,255,255));
            screen.blit(set_text, (0, 495));
        if set_set == 3: #나가기
            if space:
                running = False;
            screen.blit(set_text, (0, 595));
        #메인화면에서 그려야될것들
        screen.blit(butten, (320, 300));
        screen.blit(butten, (320, 400));
        screen.blit(butten, (320, 500));
        screen.blit(butten, (320, 600));
        m_t = mainfont.render("게임 시작", True , (255,255,255));
        screen.blit(m_t, (480, 305));
        m_t = mainfont.render("리듬 편집", True , (255,255,255));
        screen.blit(m_t, (480, 405));
        m_t = mainfont.render("설정", True , (255,255,255));
        screen.blit(m_t, (480, 505));
        m_t = mainfont.render("나가기", True , (255,255,255));
        screen.blit(m_t, (480, 605));
        #메인화면 코드 끝
    elif (gamepage == 2): #설정
        screen.blit(background, (0, 0));
        if down2 and not up8:
            down2 = False;
            if set_set < 6:
                set_set += 1;
            else:
                set_set = 0;
        if up8 and not down2:
            up8 = False;
            if set_set > 0:
                set_set -= 1;
            else:
                set_set = 6;
        if set_set == 0: #초당 프레임 표시
            playtext = "프레임을 보일지 숨길지 결정합니다.";
            if space:
                space = False;
                if setting[0]:
                    setting[0] = False;
                    if setting[4]:
                        print("초당 프레임 숨기기를 선택하셨습니다.")
                else:
                    setting[0] = True;
                    if setting[4]:
                        print("초당 프레임 보이기를 선택하셨습니다.")
            screen.blit(set_text, (0, 95));
        if set_set == 1: #초당 프레임 제한
            playtext = "초당 프레임을 제한합니다.";
            if space:
                space = False;
                if fpstick == 30:
                    set_set = 0;
                elif fpstick == 60:
                    set_set = 1;
                elif fpstick == 120:
                    set_set = 2;
                elif fpstick == 144:
                    set_set = 3;
                elif fpstick == 244:
                    set_set = 4;
                gamepage = 3;
                intro1 = mainfont.render("초당 프레임 제한 설정", True , (255, 255, 255));
                intro2 = mainfont.render("선택후 스페이스바!" ,True,(255,255,255));
                intro3 = mainfont.render("초당 30",True,(255,255,255));
                intro4 = mainfont.render("초당 60",True,(255,255,255));
                intro5 = mainfont.render("초당 120",True,(255,255,255));
                intro6 = mainfont.render("초당 144",True,(255,255,255));
                intro7 = mainfont.render("초당 244",True,(255,255,255));
                if setting[4]:
                    print("프레임 제한 설정을 선택하셨습니다.")
            screen.blit(set_text, (0, 195));
        if set_set == 2: #ESC키 강제종료 기능
            playtext = "esc키를 누르면 게임을 종료할지 선택합니다.";
            if space:
                space = False;
                if setting[1]:
                    setting[1] = False;
                else:
                    setting[1] = True;
            screen.blit(set_text, (0, 295));
        if set_set == 3: #배경음악 재생
            playtext = "배경음악을 재생할지 중지할지 선택합니다."
            if space:
                space = False;
                if setting[2]:
                    setting[2] = False;
                    pygame.mixer.music.stop();
                else:
                    setting[2] = True;
                    pygame.mixer.music.play(-1);
            screen.blit(set_text, (0, 395));
        if set_set == 4: #기록 및 정보
            playtext = "기록 및 정보를 봅니다.";
            if space:
                space = False;
                gamepage = 4;
                intro1 = mainfont.render("사이트: http://jrce.614.kro.kr",True,(255,255,255));
                intro2 = mainfont.render("제작자: 쥰니(614)",True,(255,255,255));
                intro3 = mainfont.render("버전:" + version,True,(255,255,255));
                intro4 = mainfont.render("기록 및 정보", True ,(255,255,255));
            screen.blit(set_text, (0, 495));
        if set_set == 5: #콘솔 로그 표시
            playtext = "음..."
            if space:
                space = False;
            screen.blit(set_text, (0, 595));
        if set_set == 6: #설정 나가기
            playtext = "설정을 나갑니다."
            if space:
                space = False;
                set_set = 0;
                gamepage = 1;
                if setting[4]:
                    print("설정을 나갔습니다.")
                    print("메인화면에 들어왔습니다.")
            screen.blit(set_text, (0, 695));
        #설정화면에서 그려야 될것들
        screen.blit(butten, (320 , 100));
        screen.blit(butten, (320 , 200));
        screen.blit(butten, (320 , 300));
        screen.blit(butten, (320 , 400));
        screen.blit(butten, (320 , 500));
        screen.blit(butten, (320 , 600));
        screen.blit(butten, (320 , 700));
        if setting[0]:
            m_t = mainfont.render("초당 프레임 숨기기", True ,(255, 255, 255));
        else:
            m_t = mainfont.render("초당 프레임 보이기", True ,(255, 255, 255));
        screen.blit(m_t, (480 , 105));
        screen.blit(music1, (480 , 205));
        if setting[1]:
            m_t = mainfont.render("esc키 종료 중지", True , (255,255,255));
        else:
            m_t = mainfont.render("esc키 종료 사용", True , (255,255,255));
        screen.blit(m_t, (480 , 305))
        if setting[2]:
            m_t = mainfont.render("배경음악 종료하기" , True , (255,255,255));
        else:
            m_t = mainfont.render("배경음악 재생하기" , True , (255,255,255));
        screen.blit(m_t, (480, 405));
        screen.blit(music2, (480, 505));
        if setting[4]:
            m_t = mainfont.render("미완", True ,(255, 255, 255));
        else:
            m_t = mainfont.render("미완", True, (255, 255, 255));
        screen.blit(m_t, (480 , 605));
        screen.blit(music3, (480, 705));
        m_t = mainfont.render(playtext, True , (255,255,255));
        playtext = m_t.get_rect().size;
        screen.blit(m_t, ((800 - playtext[0] / 2), 805));
        playtext = "로딩중..."
        screen.blit(music4, (720, 10));
        #설정 코드 끝
    elif (gamepage == 3): #프레임 제한 설정, 30, 60 ,120, 144, 244
        screen.blit(background, (0 ,0))
        if down2 and not up8:
            down2 = False;
            if set_set  < 4:   
                set_set += 1;
            else:
                set_set = 0;
        if up8 and not down2:
            up8 = False;
            if set_set > 0:
                set_set -= 1;
            else:
                set_set = 4;
        if set_set == 0: #30프레임 제한
            if space:
                space = False;
                fpstick = 30;
                gamepage = 2;
                if setting[4]:
                    print("초당 30프레임 제한으로 설정하셨습니다.")    
            screen.blit(set_text, (0 , 195))
        if set_set == 1: #60프레임 제한
            if space:
                space = False;
                gamepage= 2;
                fpstick = 60;
                if setting[4]:
                    print("초당 60프레임 제한으로 설정하셨습니다.")
            screen.blit(set_text, (0 , 295))
        if set_set == 2: #120프레임 제한
            if space:
                space = False;
                gamepage = 2;
                fpstick = 120;
                if setting[4]:
                    print("초당 120프레임 제한으로 설정하셨습니다.")
                
            screen.blit(set_text, (0 , 395))
        if set_set == 3: #144프레임 제한
            if space:
                space = False;
                gamepage = 2;
                fpstick = 144;
                if setting[4]:
                    print("초당 144프레임 제한으로 설정하셨습니다.")
            screen.blit(set_text, (0 , 495))
        if set_set == 4: #244프레임 제한
            if space:
                space = False;
                gamepage = 2;
                fpstick = 244;
                if setting[4]:
                    print("초당 244프레임 제한으로 설정하셨습니다.")
            screen.blit(set_text, (0 , 595))
        #프레임 제한화면에서 그려야 될것들
        if fpstick == 30:
            screen.blit(setbutten, (320 , 200))
        else:
            screen.blit(butten, (320 , 200))
        if fpstick == 60:
            screen.blit(setbutten, (320 , 300))
        else:
            screen.blit(butten, (320 , 300))
        if fpstick == 120:
            screen.blit(setbutten, (320 , 400))
        else:    
            screen.blit(butten, (320 , 400))
        if fpstick == 144:
            screen.blit(setbutten, (320 , 500))
        else:
            screen.blit(butten, (320 , 500))
        if fpstick == 244:
            screen.blit(setbutten, (320 , 600))
        else:
            screen.blit(butten, (320 , 600))
        screen.blit(intro1, (470 , 50));
        screen.blit(intro2, (490 , 750));
        screen.blit(intro3, (480 ,205));
        screen.blit(intro4, (480, 305));
        screen.blit(intro5,(480,405));
        screen.blit(intro6,(480,505));
        screen.blit(intro7,(480,605));
        #프레임 제한설정 코드 끝
    elif (gamepage == 4):
        #기록 및 정보에서 그려야 될것들
        screen.blit(background, (0, 0))
        m_t = mainfont.render("게임 실행시간: " + str(round(r_time,1)), True , (255, 255, 255));
        screen.blit(m_t, (160 , 100));
        m_t = mainfont.render("곡 선택횟수: " + str(log[0]) ,True,(255,255,255));
        screen.blit(m_t, (160 , 200));
        m_t = mainfont.render("조작버튼 누른횟수: " + str(log[1]),True,(255,255,255));
        screen.blit(m_t, (160 ,300));
        m_t = mainfont.render("이전 5초동안 평균 프레임: " + str(log[2]),True,(255,255,255));
        screen.blit(m_t, (160, 400));
        screen.blit(intro1,(160,500));
        screen.blit(intro2,(160,600));
        screen.blit(intro3,(160,700)); 
        screen.blit(intro4,(620,10)); #제목
        if space:
            space = False;
            gamepage = 2;
        #기록 및 정보 코드 끝
    #곡 디렉토리 선택
    elif (gamepage == 6):
        screen.blit(background, (0,0));
        m_t = mainfont.render("즐기고 싶은 곡 디렉토리(?)를 선택하세요" , True , (255,255,255));
        screen.blit(m_t, (180 , 110));
        if down2 and not up8:
            down2 = False;
            if set_set < 2:
                set_set = 2;
            elif varvar == 0:
                set_set = 0;
            else:
                set_set = 1;
        if up8 and not down2:
            up8 = False;
            if set_set == 2:
                if varvar == 0:
                    set_set = 0;
                else:
                    set_set = 1;
            else:
                set_set = 2;
        if right6 and not left4:
            right6 = False;
            if set_set == 0:
                set_set = 1;
        elif left4 and not right6:
            left4 = False;
            if set_set == 1:
                set_set = 0;
        if set_set == 0:
            varvar = 0;
            if space:
                space = False;
                gamepage = 9;
            screen.blit(disk_set, (100, 200));
        elif set_set == 1:
            varvar = 1;
            if space:
                space = False;
                gamepage = 9;
            screen.blit(disk_set, (800, 200));
        elif set_set == 2:
            if space:
                space = False;
                set_set = 0;
                gamepage = 1;
            screen.blit(set_text, (0 , 695));
        #곡 디렉토리 선택창에서 그려야 될것들
        screen.blit(butten, (320, 700));
        m_t = mainfont.render("돌아가기", True , (255,255,255))
        screen.blit(m_t, (480, 705))
        screen.blit(localdisk_c, (100, 180));
        screen.blit(localdisk_d, (800, 200));
        #곡 디렉토리 선택 코드 끝
    elif (gamepage == 9):
        #그리고 볼것들
        screen.blit(background, (0,0));
        m_t = mainfont.render("곡 로딩중입니다...",True,(255,255,255));
        screen.blit(m_t,(10 , 800));
        pygame.display.update();
        #다그림
        #로딩할것들
        if set_set == 0:
            #음악
            music1 = pygame.mixer.Sound("music/i_1f1e33.mp3");
            music2 = pygame.mixer.Sound("music/i_knight_rider.mp3");
            music3 = pygame.mixer.Sound("music/i_cyaegha.mp3");
            music4 = pygame.mixer.Sound("music/i_izana.mp3")
            music5 = pygame.mixer.Sound("music/i_os.mp3");
            #이미지
            intro1 = pygame.image.load("data/1f1e33.png");
            intro2 = pygame.image.load("data/knight_rider.jpg");
            intro3 = pygame.image.load("data/cyaegha.jpg");
            intro4 = pygame.image.load("data/izana.jpg");
            intro5 = pygame.image.load("data/os.png");
            #곡리스트
            musiclist = ["#1f1e33", "Knight_Rider" , "Cyaegha" , "IZANA" , "Oshama Scramble!" , "미정" , "미정" ,"미정" ,"미정" , "나가기"];
            composer = ["Camellia" , "USAO" , "USAO" , "t+pazolite vs P*Light" ,"t+pazolite" ,"미정" , "미정" , "미정" , "미정" , "나가실려면 스페이스바!"]; 
            #렌더링, 렌더링을 외하냐? 미리 렌더링 해놓으면 두번다신 렌더를 안해도 되고 성능절약임 ㅇㅅㅇ
            render[0] = mainfont.render(musiclist[0], True, (255,255,255));
            render[1] = mainfont.render(musiclist[1], True, (255,255,255));
            render[2] = mainfont.render(musiclist[2], True, (255,255,255));
            render[3] = mainfont.render(musiclist[3], True, (255,255,255));
            render[4] = mainfont.render(musiclist[4], True, (255,255,255));
            render[5] = mainfont.render(musiclist[5], True, (255,255,255));
            render[6] = mainfont.render(musiclist[6], True, (255,255,255));
            render[7] = mainfont.render(musiclist[7], True, (255,255,255));
            render[8] = mainfont.render(musiclist[8], True, (255,255,255));
            #페이지 변경
            gamepage = 10;
        elif set_set == 1:
            pass;
        pygame.mixer.music.stop(); 
        playsound = -1;
        set_set = 0; #언젠가 저장기능이 만들어지면 삭제할 예정, 저장기능이 만들어지면 저장기능에 마지막으로 몇번째 곡을 선택하다 나갔는지 저장하고 나중에 다시 올떄 선택해두었던 곡 위치로 선택할예정인데 아... 미래의 쥰니야 이해되지? 제발 저장기능 만들면 삭제해줘 :)
    #곡 디렉토리 (재사용 가능)
    elif (gamepage == 10):
        #처음에 그려야될것
        screen.blit(background, (0 , 0));
        screen.blit(set_text, (0 , 400));
        #조작 코드
        if up8 and not down2:
            up8 = False;
            if set_set < 1:
               set_set = 8;
            else:
                set_set -= 1;
        elif down2 and not up8:
            down2 = False;
            if set_set > 7:
                set_set = 0;
            else:
                set_set += 1;
        #곡들
        if set_set == 0: #1f1e33
            screen.blit(intro1, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music1.play(-1);
            gotoplaying();
        elif set_set == 1: #knight rider
            screen.blit(intro2, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music2.play(-1);
            gotoplaying();
        elif set_set == 2: #cyaegha
            screen.blit(intro3, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music3.play(-1);
            gotoplaying();
        elif set_set == 3: #izana
            screen.blit(intro4, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music4.play(-1);
            gotoplaying();
        elif set_set == 4:
            screen.blit(intro5, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music5.play(-1);
            gotoplaying();
        elif set_set == 5:
            screen.blit(intro6, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music6.play(-1);
            gotoplaying();
        elif set_set == 6:
            screen.blit(intro7, (100,200));
            if playsound != set_set:
                playsound = set_set;
                music7.play(-1);
            gotoplaying();
        if varvar != playsound:
            if varvar == 0:
                music1.stop();
            elif varvar == 1:
                music2.stop();
            elif varvar == 2:
                music3.stop();
            elif varvar == 3:
                music4.stop();
            elif varvar == 4:
                music5.stop();
            elif varvar == 5:
                music6.stop();
            elif varvar == 6:
                music7.stop();
            elif varvar == 7:
                music8.stop();
            elif varvar == 8:
                music9.stop();
            varvar = playsound;
        #곡 디렉토리 C: 에서 그려야될것들
        #바
        screen.blit(butten, (900, 405)); #가운데바
        m_t = fpsfont.render(composer[set_set] , True , (255,255,255))
        screen.blit(m_t, (100,150))
        m_t = mainfont.render(musiclist[set_set], True , (255,255,255));
        screen.blit(m_t, (100,80));
        #바에 텍스트 그리기
        screen.blit(m_t, (1060,405)); #이미 위 코드에 렌더링 함 그래서 렌더 할필요가 없음
        if set_set > 0: #위
            screen.blit(butten, (920 ,305)); #바
            screen.blit(render[set_set - 1], (1080,305)); #글자출력
        if set_set > 1: #위위
            screen.blit(butten, (940 ,205)); #바
            screen.blit(render[set_set - 2], (1100,205)); #글자출력
        if set_set > 2: #맨위 한칸아레
            screen.blit(butten, (960 ,105)); #바
            screen.blit(render[set_set - 3], (1120,105)); #글자출력
        if set_set > 3: #맨위
            screen.blit(butten, (980 ,5)); #바
            screen.blit(render[set_set - 4], (1140,5)); #글자출력
        if set_set < 10: #아레
            screen.blit(butten, (880, 505)); #아레바
            screen.blit(render[set_set + 1], (1040,505)); #글자출력
        if set_set < 9: #아레아레
            screen.blit(butten, (860, 605)); #아레아레바
            screen.blit(render[set_set + 2], (1020,605)); #글자출력
        if set_set < 8: #맨아레 한칸위
            screen.blit(butten, (840, 705)); #맨아레바
            screen.blit(render[set_set + 3], (1000,705)); #글자출력
        if set_set < 7: #맨아레
            screen.blit(butten, (820, 805)); #맨아레바
            screen.blit(render[set_set + 4], (980,805)); #글자출력
        #곡 디렉토리 C: 코드 끝
    elif (gamepage == 11): #추가된 곡 디렉토리
        pass;
    elif (gamepage == 19):
        screen.blit(background, (0 , 0));
        m_t = mainfont.render("로딩중입니다...", True , (255,255,255));
        pygame.display.update();
        if set_set == 0:
            music1 = pygame.mixer.Sound("music/1f1e33.mp3"); #music1은 기본 음악
            music2 = "1f1e33"; #music2는 음악 제목
            intro1 = pygame.image.load("data/1f1e33.png"); #intro1 은 음악 사진
            intro2 = 1; #intro2는 곡 넘버
            render[0] = mainfont.render(music2,True,(255,255,255));
        elif set_set == 1:
            music1 = pygame.mixer.Sound("music/knight_rider.mp3");
        elif set_set == 2:
            music1 = pygame.mixer.Sound("music/cyaegha.mp3");
        gamepage = 20;
        screen.blit(m_t,(10 , 800));
    #리겜 시작
    elif (gamepage == 20): #리듬게임 시작!
        screen.blit(background, (0 , 0));
        screen.blit(text_background,(880, 10))
        screen.blit(render[0], (1100,20))
        if intro2 == 1:
            notebutten();
            pygame.display.update();
    elif (gamepage == 30): #리듬편집
        screen.blit(background, (0,0));
        #screen.blit(intro1, (20, 680));
        #screen.blit(intro2, (20,780));
        #if r_time > varvar or space:
        #    space = False;
        #    gamepage = 1; set_set = 0;
        
    elif (gamepage == 40): #예외처리 한 코드에서 오류감지시
        screen.blit(background, (0, 0));
        m_t = mainfont.render(playtext, True , (255,255,255));
        set_set = m_t.get_rect().size;
        set_set = set_set[0] / 2
        screen.blit(m_t, (set_set , 410));
    #마지막으로 띄울것
    if setting[0]: #초당 프레임 표시
        fps = fpsfont.render(str(int(clock.get_fps())), True , (255, 100, 100)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 10));
        fps = fpsfpsfont.render( str(fpsfps[5]) , True , (255, 250, 250)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 50));
        fps = fpsfpsfont.render( str(fpsfps[4]) , True , (255, 250, 250)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 80));
        fps = fpsfpsfont.render( str(fpsfps[3]), True , (255, 250, 250)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 110));
        fps = fpsfpsfont.render( str(fpsfps[2]), True , (255, 250, 250)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 140));
        fps = fpsfpsfont.render( str(fpsfps[1]), True , (255, 250, 250)); #fps , 폰트.랜더링(문자 , 참 , 색깔)
        screen.blit(fps, (10, 170));
    
    if fpsfps[0] < int(r_time): #5초내 평균 초당프레임
        fpsfps[0] = int(r_time);
        fpsfps[1] = fpsfps[2]; fpsfps[2] = fpsfps[3]; fpsfps[3] = fpsfps[4]; fpsfps[4] = fpsfps[5]; fpsfps[5] = int(clock.get_fps()); #변환
        log[2] = (fpsfps[1] + fpsfps[2] + fpsfps[3] + fpsfps[4] + fpsfps[5]) / 5; #통계
    #타이머
    r_time = (pygame.time.get_ticks() - s_time) / 1000 #시간(ms)를 초(s)로 표시하기 위에 1000으로 나눔
    #디스플레이 리프레쉬
    pygame.display.update();
pygame.quit(); #끝
