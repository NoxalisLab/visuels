"""English 1080x1080 visual for X — Mittwald breached via its MCP server (Nov 2026)."""
from PIL import Image, ImageDraw, ImageFont
W=H=1080; S=2
FD='/workspace/hecadium-visuels-src/fonts/'
F=lambda n,s: ImageFont.truetype({'sansb':FD+'font-5.ttf','sanssb':FD+'font-4.ttf','sans':FD+'font-2.ttf','mono':FD+'font-1.ttf'}[n], int(s*S))
BG=(17,20,24); ACC=(145,169,191); WH=(255,255,255); YEL=(246,201,72); RED=(220,50,47); MUT=(140,150,162); TXT=(236,239,242)
im=Image.new('RGB',(W*S,H*S),BG); d=ImageDraw.Draw(im,'RGBA')
for x in range(0,W,60): d.line([(x*S,0),(x*S,H*S)],fill=ACC+(14,),width=S)
for y in range(0,H,60): d.line([(0,y*S),(W*S,y*S)],fill=ACC+(14,),width=S)
def T(xy,txt,f,col,a=1,anchor='mm'): d.text((xy[0]*S,xy[1]*S),txt,font=f,fill=col+(int(255*a),),anchor=anchor)
def R(b,col,r,a=1,out=None,w=2): d.rounded_rectangle([b[0]*S,b[1]*S,b[2]*S,b[3]*S],r*S,fill=col+(int(255*a),) if col else None,outline=out,width=w*S)
def arrow(x1,y1,x2,y2,col=(120,128,140,255)):
    d.line([(x1*S,y1*S),(x2*S,y2*S)],fill=col,width=4*S)
    d.polygon([(x2*S,(y2-12)*S),(x2*S,(y2+12)*S),((x2+12)*S,y2*S)],fill=col)
T((540,60),'@hecadium · @NoxalisLab · @SecLeap',F('sanssb',26),TXT,0.9)
R((60,110,340,300),(28,34,42),20,1,out=(90,100,112),w=2)
T((200,170),'AI assistant',F('sanssb',30),WH); T((200,215),'of a customer',F('sans',24),MUT); T((200,260),'(or an attacker)',F('sanssb',24),YEL)
arrow(345,205,385,205)
R((400,110,680,300),(40,22,24),20,1,out=RED,w=3)
T((540,170),'MCP server',F('sanssb',30),WH); T((540,215),'built by the host',F('sans',24),MUT); T((540,260),'flaw exploited',F('sanssb',24),RED)
arrow(685,205,725,205)
R((740,110,1020,300),(28,34,42),20,1,out=(90,100,112),w=2)
T((880,170),'Hosting panel',F('sanssb',30),WH); T((880,215),'mStudio, SSH',F('sans',24),MUT); T((880,260),'56 projects hit',F('sanssb',24),YEL)
R((60,340,1020,560),(0,0,0),28,0.55)
T((540,400),'Web host breached through',F('sansb',50),WH)
T((540,465),'its own AI connector',F('sansb',50),YEL)
T((540,525),'8 days undetected, attackers back on Nov 12',F('sanssb',28),TXT)
R((60,590,1020,940),(20,24,30),24,0.9)
T((540,635),'If you expose an MCP server:',F('sansb',36),WH)
for k,l in enumerate(['Treat it like a public API','Least-privilege token per tool','No shell or file access by default','Alert on machine-speed sessions']):
    T((120,700+k*55),'- '+l,F('sanssb',30),TXT,1,'lm')
T((540,985),'Sources: Mittwald status page and blog, The Record, heise, Nov 2026',F('sans',24),MUT)
im=im.resize((W,H),Image.LANCZOS); im.save('x-visual-mittwald-mcp.png'); print('ok')
