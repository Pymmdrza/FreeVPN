import time
from rich.console import Console
import requests
from lxml import html


console = Console()


respone_block = requests.get("https://ipspeed.info/freevpn_l2tpipsec.php?language=en")
byte_string = respone_block.content
source_code = html.fromstring(byte_string)
xpatch_country1 = '/html/body/center/div[6]/div[3]/div[7]'
xpatch_country2 = '/html/body/center/div[6]/div[3]/div[13]'
xpatch_country3 = '/html/body/center/div[6]/div[3]/div[19]'
xpatch_country4 = '/html/body/center/div[6]/div[3]/div[25]'
xpatch_country5 = '/html/body/center/div[6]/div[3]/div[31]'
xpatch_country6 = '/html/body/center/div[6]/div[3]/div[37]'
xpatch_country7 = '/html/body/center/div[6]/div[3]/div[43]'
xpatch_country8 = '/html/body/center/div[6]/div[3]/div[49]'
xpatch_country9 = '/html/body/center/div[6]/div[3]/div[55]'
# ============================================================
xpatch_2country1 = '/html/body/center/div[6]/div[3]/div[66]'
xpatch_2country2 = '/html/body/center/div[6]/div[3]/div[72]'
xpatch_2country3 = '/html/body/center/div[6]/div[3]/div[78]'
xpatch_2country4 = '/html/body/center/div[6]/div[3]/div[84]'
xpatch_2country5 = '/html/body/center/div[6]/div[3]/div[90]'
xpatch_2country6 = '/html/body/center/div[6]/div[3]/div[96]'
xpatch_2country7 = '/html/body/center/div[6]/div[3]/div[102]'
xpatch_2country8 = '/html/body/center/div[6]/div[3]/div[108]'
xpatch_ip1 = '/html/body/center/div[6]/div[3]/div[8]'
xpatch_ip2 = '/html/body/center/div[6]/div[3]/div[14]'
xpatch_ip3 = '/html/body/center/div[6]/div[3]/div[20]'
xpatch_ip4 = '/html/body/center/div[6]/div[3]/div[26]'
xpatch_ip5 = '/html/body/center/div[6]/div[3]/div[32]'
xpatch_ip6 = '/html/body/center/div[6]/div[3]/div[38]'
xpatch_ip7 = '/html/body/center/div[6]/div[3]/div[44]'
xpatch_ip8 = '/html/body/center/div[6]/div[3]/div[50]'
xpatch_ip9 = '/html/body/center/div[6]/div[3]/div[56]'
xpatch_2ip1 = '/html/body/center/div[6]/div[3]/div[67]'
xpatch_2ip2 = '/html/body/center/div[6]/div[3]/div[73]'
xpatch_2ip3 = '/html/body/center/div[6]/div[3]/div[79]'
xpatch_2ip4 = '/html/body/center/div[6]/div[3]/div[85]'
xpatch_2ip5 = '/html/body/center/div[6]/div[3]/div[91]'
xpatch_2ip6 = '/html/body/center/div[6]/div[3]/div[97]'
xpatch_2ip7 = '/html/body/center/div[6]/div[3]/div[103]'
xpatch_2ip8 = '/html/body/center/div[6]/div[3]/div[109]'

xpatch_uptime1 = '/html/body/center/div[6]/div[3]/div[9]'
xpatch_uptime2 = '/html/body/center/div[6]/div[3]/div[15]'
xpatch_uptime3 = '/html/body/center/div[6]/div[3]/div[21]'
xpatch_uptime4 = '/html/body/center/div[6]/div[3]/div[27]'
xpatch_uptime5 = '/html/body/center/div[6]/div[3]/div[33]'
xpatch_uptime6 = '/html/body/center/div[6]/div[3]/div[39]'
xpatch_uptime7 = '/html/body/center/div[6]/div[3]/div[45]'
xpatch_uptime8 = '/html/body/center/div[6]/div[3]/div[51]'
xpatch_uptime9 = '/html/body/center/div[6]/div[3]/div[57]'
xpatch_ping1 = '/html/body/center/div[6]/div[3]/div[10]'
xpatch_ping2 = '/html/body/center/div[6]/div[3]/div[16]'
xpatch_ping3 = '/html/body/center/div[6]/div[3]/div[22]'
xpatch_ping4 = '/html/body/center/div[6]/div[3]/div[28]'
xpatch_ping5 = '/html/body/center/div[6]/div[3]/div[34]'
xpatch_ping6 = '/html/body/center/div[6]/div[3]/div[40]'
xpatch_ping7 = '/html/body/center/div[6]/div[3]/div[46]'
xpatch_ping8 = '/html/body/center/div[6]/div[3]/div[52]'
xpatch_ping9 = '/html/body/center/div[6]/div[3]/div[58]'
xpatch_2uptime1 = '/html/body/center/div[6]/div[3]/div[68]'
xpatch_2uptime2 = '/html/body/center/div[6]/div[3]/div[74]'
xpatch_2uptime3 = '/html/body/center/div[6]/div[3]/div[80]'
xpatch_2uptime4 = '/html/body/center/div[6]/div[3]/div[86]'
xpatch_2uptime5 = '/html/body/center/div[6]/div[3]/div[92]'
xpatch_2uptime6 = '/html/body/center/div[6]/div[3]/div[98]'
xpatch_2uptime7 = '/html/body/center/div[6]/div[3]/div[104]'
xpatch_2uptime8 = '/html/body/center/div[6]/div[3]/div[110]'
xpatch_2ping1 = '/html/body/center/div[6]/div[3]/div[69]'
xpatch_2ping2 = '/html/body/center/div[6]/div[3]/div[75]'
xpatch_2ping3 = '/html/body/center/div[6]/div[3]/div[81]'
xpatch_2ping4 = '/html/body/center/div[6]/div[3]/div[87]'
xpatch_2ping5 = '/html/body/center/div[6]/div[3]/div[93]'
xpatch_2ping6 = '/html/body/center/div[6]/div[3]/div[99]'
xpatch_2ping7 = '/html/body/center/div[6]/div[3]/div[105]'
xpatch_2ping8 = '/html/body/center/div[6]/div[3]/div[111]'

tree_country1 = source_code.xpath(xpatch_country1)
xcountry1 = tree_country1[0].text_content()

tree_country2 = source_code.xpath(xpatch_country2)
xcountry2 = tree_country2[0].text_content()

tree_country3 = source_code.xpath(xpatch_country3)
xcountry3 = tree_country3[0].text_content()

tree_country4 = source_code.xpath(xpatch_country4)
xcountry4 = tree_country4[0].text_content()

tree_country5 = source_code.xpath(xpatch_country5)
xcountry5 = tree_country5[0].text_content()

tree_country6 = source_code.xpath(xpatch_country6)
xcountry6 = tree_country6[0].text_content()

tree_country7 = source_code.xpath(xpatch_country7)
xcountry7 = tree_country7[0].text_content()

tree_country8 = source_code.xpath(xpatch_country8)
xcountry8 = tree_country8[0].text_content()

tree_ip1 = source_code.xpath(xpatch_ip1)
xip1 = tree_ip1[0].text_content()

tree_ip2 = source_code.xpath(xpatch_ip2)
xip2 = tree_ip2[0].text_content()

tree_ip3 = source_code.xpath(xpatch_ip3)
xip3 = tree_ip3[0].text_content()

tree_ip4 = source_code.xpath(xpatch_ip4)
xip4 = tree_ip4[0].text_content()

tree_ip5 = source_code.xpath(xpatch_ip5)
xip5 = tree_ip5[0].text_content()

tree_ip6 = source_code.xpath(xpatch_ip6)
xip6 = tree_ip6[0].text_content()

tree_ip7 = source_code.xpath(xpatch_ip7)
xip7 = tree_ip7[0].text_content()

tree_ip8 = source_code.xpath(xpatch_ip8)
xip8 = tree_ip8[0].text_content()

tree_ping1 = source_code.xpath(xpatch_ping1)
xping1 = tree_ping1[0].text_content()

tree_ping2 = source_code.xpath(xpatch_ping2)
xping2 = tree_ping2[0].text_content()

tree_ping3 = source_code.xpath(xpatch_ping3)
xping3 = tree_ping3[0].text_content()

tree_ping4 = source_code.xpath(xpatch_ping4)
xping4 = tree_ping4[0].text_content()

tree_ping5 = source_code.xpath(xpatch_ping5)
xping5 = tree_ping5[0].text_content()

tree_ping6 = source_code.xpath(xpatch_ping6)
xping6 = tree_ping6[0].text_content()

tree_ping7 = source_code.xpath(xpatch_ping7)
xping7 = tree_ping7[0].text_content()

tree_ping8 = source_code.xpath(xpatch_ping8)
xping8 = tree_ping8[0].text_content()

tree_uptime1 = source_code.xpath(xpatch_uptime1)
xuptime1 = tree_uptime1[0].text_content()

tree_uptime2 = source_code.xpath(xpatch_uptime2)
xuptime2 = tree_uptime2[0].text_content()

tree_uptime3 = source_code.xpath(xpatch_uptime3)
xuptime3 = tree_uptime3[0].text_content()

tree_uptime4 = source_code.xpath(xpatch_uptime4)
xuptime4 = tree_uptime4[0].text_content()

tree_uptime5 = source_code.xpath(xpatch_uptime5)
xuptime5 = tree_uptime5[0].text_content()

tree_uptime6 = source_code.xpath(xpatch_uptime6)
xuptime6 = tree_uptime6[0].text_content()

tree_uptime7 = source_code.xpath(xpatch_uptime7)
xuptime7 = tree_uptime7[0].text_content()

tree_uptime8 = source_code.xpath(xpatch_uptime8)
xuptime8 = tree_uptime8[0].text_content()

tree_uptime9 = source_code.xpath(xpatch_uptime9)
xuptime9 = tree_uptime9[0].text_content()
# ==================
tree_2uptime1 = source_code.xpath(xpatch_2uptime1)
x2uptime1 = tree_2uptime1[0].text_content()

tree_2uptime2 = source_code.xpath(xpatch_2uptime2)
x2uptime2 = tree_2uptime2[0].text_content()

tree_2uptime3 = source_code.xpath(xpatch_2uptime3)
x2uptime3 = tree_2uptime3[0].text_content()

tree_2uptime4 = source_code.xpath(xpatch_2uptime4)
x2uptime4 = tree_2uptime4[0].text_content()

tree_2uptime5 = source_code.xpath(xpatch_2uptime5)
x2uptime5 = tree_2uptime5[0].text_content()

tree_2uptime6 = source_code.xpath(xpatch_2uptime6)
x2uptime6 = tree_2uptime6[0].text_content()

tree_2uptime7 = source_code.xpath(xpatch_2uptime7)
x2uptime7 = tree_2uptime7[0].text_content()

# ---------------------------------------------
tree_2country1 = source_code.xpath(xpatch_2country1)
x2country1 = tree_2country1[0].text_content()

tree_2country2 = source_code.xpath(xpatch_2country2)
x2country2 = tree_2country2[0].text_content()

tree_2country3 = source_code.xpath(xpatch_2country3)
x2country3 = tree_2country3[0].text_content()

tree_2country4 = source_code.xpath(xpatch_2country4)
x2country4 = tree_2country4[0].text_content()

tree_2country5 = source_code.xpath(xpatch_2country5)
x2country5 = tree_2country5[0].text_content()

tree_2country6 = source_code.xpath(xpatch_2country6)
x2country6 = tree_2country6[0].text_content()

tree_2country7 = source_code.xpath(xpatch_2country7)
x2country7 = tree_2country7[0].text_content()

# ----------------------------------------------
tree_2ip1 = source_code.xpath(xpatch_2ip1)
x2ip1 = tree_2ip1[0].text_content()

tree_2ip2 = source_code.xpath(xpatch_2ip2)
x2ip2 = tree_2ip2[0].text_content()

tree_2ip3 = source_code.xpath(xpatch_2ip3)
x2ip3 = tree_2ip3[0].text_content()

tree_2ip4 = source_code.xpath(xpatch_2ip4)
x2ip4 = tree_2ip4[0].text_content()

tree_2ip5 = source_code.xpath(xpatch_2ip5)
x2ip5 = tree_2ip5[0].text_content()

tree_2ip6 = source_code.xpath(xpatch_2ip6)
x2ip6 = tree_2ip6[0].text_content()

tree_2ip7 = source_code.xpath(xpatch_2ip7)
x2ip7 = tree_2ip7[0].text_content()

# ---------------------------------------
tree_2ping1 = source_code.xpath(xpatch_2ping1)
x2ping1 = tree_2ping1[0].text_content()

tree_2ping2 = source_code.xpath(xpatch_2ping2)
x2ping2 = tree_2ping2[0].text_content()

tree_2ping3 = source_code.xpath(xpatch_2ping3)
x2ping3 = tree_2ping3[0].text_content()

tree_2ping4 = source_code.xpath(xpatch_2ping4)
x2ping4 = tree_2ping4[0].text_content()

tree_2ping5 = source_code.xpath(xpatch_2ping5)
x2ping5 = tree_2ping5[0].text_content()

tree_2ping6 = source_code.xpath(xpatch_2ping6)
x2ping6 = tree_2ping6[0].text_content()

tree_2ping7 = source_code.xpath(xpatch_2ping7)
x2ping7 = tree_2ping7[0].text_content()

# ================================================ #
preSharedKey = 'vpn'
username = 'vpn'
password = 'vpn'
# ================================================ #
count1 = str(xcountry1)
up1 = str(xuptime1)
ping1 = str(xping1)
ip1 = str(xip1)

count2 = str(xcountry2)
up2 = str(xuptime2)
ping2 = str(xping2)
ip2 = str(xip2)

count3 = str(xcountry3)
up3 = str(xuptime3)
ping3 = str(xping3)
ip3 = str(xip3)

count4 = str(xcountry4)
up4 = str(xuptime4)
ping4 = str(xping4)
ip4 = str(xip4)

count5 = str(xcountry5)
up5 = str(xuptime5)
ping5 = str(xping5)
ip5 = str(xip5)

count6 = str(xcountry6)
up6 = str(xuptime6)
ping6 = str(xping6)
ip6 = str(xip6)

count7 = str(xcountry7)
up7 = str(xuptime7)
ping7 = str(xping7)
ip7 = str(xip7)

count8 = str(xcountry8)
up8 = str(xuptime8)
ping8 = str(xping8)
ip8 = str(xip8)

count10 = str(x2country1)
up10 = str(x2uptime1)
ping10 = str(x2ping1)
ip10 = str(x2ip1)

count11 = str(x2country2)
up11 = str(x2uptime2)
ping11 = str(x2ping2)
ip11 = str(x2ip2)

count12 = str(x2country3)
up12 = str(x2uptime3)
ping12 = str(x2ping3)
ip12 = str(x2ip3)

count13 = str(x2country4)
up13 = str(x2uptime4)
ping13 = str(x2ping4)
ip13 = str(x2ip4)

count14 = str(x2country5)
up14 = str(x2uptime5)
ping14 = str(x2ping5)
ip14 = str(x2ip5)

count15 = str(x2country6)
up15 = str(x2uptime6)
ping15 = str(x2ping6)
ip15 = str(x2ip6)

count16 = str(x2country7)
up16 = str(x2uptime7)
ping16 = str(x2ping7)
ip16 = str(x2ip7)

from rich.console import Console

console = Console()
z = 1
for i in range(0, 2):
    time.sleep(1)
    console.print(
        '[cyan]Country: [/][gold1]' + str(count1) + '[/][white]  IP: [gold1]' + str(ip1) + '[/][green]  \nUPTIME: [/][i white]' + str(up1) + '[/][green] Ping:[/][gold1] ' + str(ping1) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count2) + '[/][white]  IP: [gold1]' + str(ip2) + '[/][green]  \nUPTIME: [/][i white]' + str(up2) + '[/][green] Ping:[/][gold1] ' + str(ping2) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count3) + '[/][white]  IP: [gold1]' + str(ip3) + '[/][green]  \nUPTIME: [/][i white]' + str(up3) + '[/][green] Ping:[/][gold1] ' + str(ping3) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count4) + '[/][white]  IP: [gold1]' + str(ip4) + '[/][green]  \nUPTIME: [/][i white]' + str(up4) + '[/][green] Ping:[/][gold1] ' + str(ping4) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count5) + '[/][white]  IP: [gold1]' + str(ip5) + '[/][green]  \nUPTIME: [/][i white]' + str(up5) + '[/][green] Ping:[/][gold1] ' + str(ping5) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count6) + '[/][white]  IP: [gold1]' + str(ip6) + '[/][green]  \nUPTIME: [/][i white]' + str(up6) + '[/][green] Ping:[/][gold1] ' + str(ping6) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count7) + '[/][white]  IP: [gold1]' + str(ip7) + '[/][green]  \nUPTIME: [/][i white]' + str(up7) + '[/][green] Ping:[/][gold1] ' + str(ping7) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count8) + '[/][white]  IP: [gold1]' + str(ip8) + '[/][green]  \nUPTIME: [/][i white]' + str(up8) + '[/][green] Ping:[/][gold1] ' + str(ping8) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count10) + '[/][white] IP: [gold1]' + str(ip10) + '[/][green]  \nUPTIME: [/][i white]' + str(up10) + '[/][green] Ping:[/][gold1] ' + str(ping10) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count11) + '[/][white] IP: [gold1]' + str(ip11) + '[/][green]  \nUPTIME: [/][i white]' + str(up11) + '[/][green] Ping:[/][gold1] ' + str(ping11) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count12) + '[/][white] IP: [gold1]' + str(ip12) + '[/][green]  \nUPTIME: [/][i white]' + str(up12) + '[/][green] Ping:[/][gold1] ' + str(ping12) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count13) + '[/][white] IP: [gold1]' + str(ip13) + '[/][green]  \nUPTIME: [/][i white]' + str(up13) + '[/][green] Ping:[/][gold1] ' + str(ping13) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count14) + '[/][white] IP: [gold1]' + str(ip14) + '[/][green]  \nUPTIME: [/][i white]' + str(up14) + '[/][green] Ping:[/][gold1] ' + str(ping14) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')

    console.print(
        '[cyan]Country: [/][gold1]' + str(count15) + '[/][white] IP: [gold1]' + str(ip15) + '[/][green]  \nUPTIME: [/][i white]' + str(up15) + '[/][green] Ping:[/][gold1] ' + str(ping15) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')
    console.print(
        '[cyan]Country: [/][gold1]' + str(count16) + '[/][white] IP: [gold1]' + str(ip16) + '[/][green]  \nUPTIME: [/][i white]' + str(up16) + '[/][green] Ping:[/][gold1] ' + str(ping16) + '[/]\n[red1]Username: [/][gold1]' + str(username) + '[/][red1]  Password: [/][gold1]' + str(password) + '[/] PreSharedKey : ' + str(preSharedKey))
    time.sleep(1)
    console.print('+----------------( MMDRZA.CoM )----------------+')
    with open("VPN_Details_Mmdrza.txt", "a") as fx:
        fx.write(f'''
        
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count1}
IP : {ip1}
UPTime : {up1}
Ping : {ping1}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count2}
IP : {ip2}
UPTime : {up2}
Ping : {ping2}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count3}
IP : {ip3}
UPTime : {up3}
Ping : {ping3}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count4}
IP : {ip4}
UPTime : {up4}
Ping : {ping4}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count5}
IP : {ip5}
UPTime : {up5}
Ping : {ping5}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country:{count6}
IP : {ip6}
UPTime : {up6}
Ping : {ping6}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count7}
IP : {ip7}
UPTime : {up7}
Ping : {ping7}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count8}
IP : {ip8}
UPTime : {up8}
Ping : {ping8}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count10}
IP : {ip10}
UPTime : {up10}
Ping : {ping10}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count11}
IP : {ip11}
UPTime : {up11}
Ping : {ping11}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count12}
IP : {ip12}
UPTime : {up12}
Ping : {ping12}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count13}
IP : {ip13}
UPTime : {up13}
Ping : {ping13}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count14}
IP : {ip14}
UPTime : {up14}
Ping : {ping14}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count15}
IP : {ip15}
UPTime : {up15}
Ping : {ping15}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
    
IPSEC and L2tp VPN ~ Programmer and Owner PyMmdrza
Country: {count16}
IP : {ip16}
UPTime : {up16}
Ping : {ping16}
Username & Password & PreSharedKey : vpn
Website : https://Mmdrza.Com
Telegram Channel : @mPython3
Telegram id : @ PyMmdrza
+-------------------------------------------------------+
        ''')
        fx.close()
