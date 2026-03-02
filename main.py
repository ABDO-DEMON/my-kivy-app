import threading, random, time
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager, FadeTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.snackbar import Snackbar
from kivy.utils import platform

# --- محرك معالجة اللغة العربية (توقيع المطور: عبدالعظيم عبدالرحمن) ---
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    def fix_ar(text):
        return get_display(arabic_reshaper.reshape(text))
except:
    def fix_ar(text): return text

# أرشيف الصيد الملكي المصنف 📜
HITS_ARCHIVE = {"FB": [], "IG": [], "TT": [], "FOLLOWERS": []}

KV = '''
MDScreenManager:
    transition: FadeTransition()
    SplashScreen:
    Dashboard:
    ControlPanel:
    HunterPro:

<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            pos_hint: {"center_x": .5, "center_y": .5}
            spacing: "25dp"
            MDIcon:
                id: splash_logo
                icon: "biohazard" 
                font_size: "160sp"
                halign: "center"
                theme_icon_color: "Custom"
                icon_color: 1, 0.84, 0, 1
                opacity: 0
            MDLabel:
                id: splash_name
                text: "ABDO DEMON V33"
                halign: "center"
                font_style: "H3"
                bold: True
                theme_text_color: "Custom"
                text_color: 1, 0.84, 0, 1
                opacity: 0

<Dashboard>:
    name: 'dash'
    on_enter: root.activate_live_ui()
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        
        # --- الشريط العلوي (التاج التفاعلي + المخطوطة المصنفة 📜) ---
        MDCard:
            size_hint: (0.96, 0.11)
            pos_hint: {"center_x": 0.5, "top": 0.98}
            md_bg_color: 0.07, 0.07, 0.07, 1
            radius: [20,]
            line_color: 1, 0.84, 0, 0.5
            line_width: 1.5
            elevation: 15

            MDBoxLayout:
                padding: "10dp"
                spacing: "10dp"
                MDCard:
                    id: crown_container
                    size_hint: (None, None)
                    size: ("55dp", "48dp")
                    md_bg_color: 0.15, 0.15, 0.15, 1
                    radius: [15,]
                    on_release: root.reveal_identity()
                    MDBoxLayout:
                        padding: "8dp"
                        MDIcon:
                            icon: "crown"
                            icon_color: 1, 0.84, 0, 1
                            font_size: "30sp"
                        MDLabel:
                            id: dev_name
                            text: ""
                            bold: True
                            theme_text_color: "Custom"
                            text_color: 1, 0.84, 0, 1
                            opacity: 0
                            adaptive_width: True
                Widget:
                MDIconButton:
                    icon: "script-text-history"
                    theme_icon_color: "Custom"
                    icon_color: 1, 0.84, 0, 1
                    on_release: app.open_classified_archive()
                MDIcon:
                    icon: "key-chain-variant"
                    icon_color: 0, 1, 1, 0.6
                    font_size: "26sp"
                    pos_hint: {"center_y": .5}

        # --- شبكة الكروت الذكية (Neon Grid) ---
        MDScrollView:
            size_hint: (1, 0.75)
            pos_hint: {"center_x": 0.5, "center_y": 0.42}
            MDGridLayout:
                cols: 2
                adaptive_height: True
                padding: "20dp"
                spacing: "25dp"

                SmartCard:
                    id: card_fb
                    icon: "facebook"
                    title: "FB HUNTER"
                    color: 0, 0.5, 1, 1
                    on_release: root.show_panel("FB HUNTER", ["Matahat Scan", "4-Chars Turbo"], "FB")

                SmartCard:
                    id: card_ig
                    icon: "instagram"
                    title: "IG ELITE"
                    color: 1, 0, 0.5, 1
                    on_release: root.show_panel("IG ELITE", ["5-Chars Hunt", "Brute Force"], "IG")

                SmartCard:
                    id: card_tt
                    icon: "tiktok"
                    title: "TT HUNTER"
                    color: 0, 1, 1, 1
                    on_release: root.show_panel("TT HUNTER", ["3-Chars Scan", "Turbo Speed"], "TT")

                SmartCard:
                    id: card_fol
                    icon: "account-star"
                    title: "FOLLOWERS"
                    color: 1, 0.84, 0, 1
                    on_release: root.show_panel("FOLLOWERS", ["Instant Inject", "API Tunnel"], "FOLLOWERS")

<SmartCard@MDCard>:
    icon: ""
    title: ""
    color: 1, 1, 1, 1
    orientation: 'vertical'
    size_hint_y: None
    height: "185dp"
    padding: "15dp"
    radius: 25
    md_bg_color: 0.05, 0.05, 0.05, 1
    line_color: self.color
    line_width: 2
    ripple_behavior: True
    MDLabel:
        id: live_ip
        text: "0.0.0.0"
        halign: "right"
        font_style: "Overline"
        theme_text_color: "Custom"
        text_color: root.color
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "50sp"
        icon_color: root.color
    MDLabel:
        text: root.title
        halign: "center"
        bold: True

<ControlPanel>:
    name: 'control'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 0.95
        MDCard:
            size_hint: (0.9, 0.6)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            md_bg_color: 0.08, 0.08, 0.08, 1
            radius: 25
            padding: "20dp"
            MDBoxLayout:
                orientation: 'vertical'
                spacing: "15dp"
                MDLabel:
                    id: panel_title
                    text: "CIPHER READY"
                    halign: "center"
                    bold: True
                    font_style: "H5"
                    theme_text_color: "Custom"
                    text_color: 1, 0.84, 0, 1
                MDBoxLayout: id: opts_box; orientation: 'vertical'; spacing: "10dp"
                MDRaisedButton:
                    text: "ABORT"
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 0.2, 0.2, 0.2, 1
                    on_release: root.manager.current = 'dash'

<HunterPro>:
    name: 'hunter_pro'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        MDLabel:
            id: engine_title
            text: "TURBO ENGINE ACTIVE"
            pos_hint: {"center_y": 0.92}
            halign: "center"
            font_style: "H5"
            bold: True
            theme_text_color: "Custom"
            text_color: 0, 1, 0.5, 1
        MDCard:
            size_hint: (0.94, 0.58)
            pos_hint: {"center_x": 0.5, "center_y": 0.48}
            md_bg_color: 0.01, 0.01, 0.01, 1
            radius: 20
            MDScrollView:
                id: scroll_view
                MDLabel:
                    id: log_stream
                    text: "> INITIALIZING V33 CIPHER..."
                    text_color: 0, 1, 0.5, 1
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size
        MDIconButton:
            icon: "stop-circle-outline"
            icon_size: "55sp"
            icon_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .1}
            on_release: root.terminate()
'''

class SplashScreen(MDScreen):
    def on_enter(self):
        Animation(opacity=1, font_size="175sp", duration=1.5, t='out_elastic').start(self.ids.splash_logo)
        Animation(opacity=1, duration=2).start(self.ids.splash_name)
        Clock.schedule_once(lambda x: setattr(self.manager, 'current', 'dash'), 4)

class Dashboard(MDScreen):
    is_expanded = False
    def activate_live_ui(self):
        Clock.schedule_interval(self.rotate_ips, 1.0)
    def rotate_ips(self, dt):
        if self.manager.current == 'dash':
            for card in [self.ids.card_fb, self.ids.card_ig, self.ids.card_tt, self.ids.card_fol]:
                card.ids.live_ip.text = f"{random.randint(10, 250)}.{random.randint(0, 255)}.XX.XX"

    def reveal_identity(self):
        if not self.is_expanded:
            self.ids.dev_name.text = fix_ar("عبدالعظيم عبدالرحمن")
            Animation(size=("310dp", "48dp"), opacity=1, duration=0.4, t='out_back').start(self.ids.crown_container)
            Animation(opacity=1, duration=0.4).start(self.ids.dev_name)
            self.is_expanded = True
        else:
            Animation(size=("55dp", "48dp"), duration=0.3).start(self.ids.crown_container)
            Animation(opacity=0, duration=0.2).start(self.ids.dev_name)
            self.is_expanded = False

    def show_panel(self, title, options, tag):
        p = self.manager.get_screen('control')
        p.ids.panel_title.text = title
        p.ids.opts_box.clear_widgets()
        for o in options:
            btn = MDRaisedButton(text=o, size_hint=(1, None), md_bg_color=(0.1, 0.1, 0.1, 1))
            btn.on_release = lambda x=title, y=o, z=tag: self.launch(x, y, z)
            p.ids.opts_box.add_widget(btn)
        self.manager.current = 'control'

    def launch(self, t, o, tag):
        h = self.manager.get_screen('hunter_pro')
        h.platform_tag = tag
        h.ids.engine_title.text = f"{t} | {o}"
        self.manager.current = 'hunter_pro'
        h.start_engine()

class ControlPanel(MDScreen): pass

class HunterPro(MDScreen):
    is_active = False
    platform_tag = ""
    def start_engine(self):
        self.is_active = True
        self.ids.log_stream.text = "> [!] CIPHER TUNNEL ACTIVE\\n> [!] ROTATING PROXIES..."
        for _ in range(5): threading.Thread(target=self.logic, daemon=True).start()

    def terminate(self):
        self.is_active = False
        self.manager.current = 'dash'

    def logic(self):
        agents = ["iPhone 17 Pro", "Android API 34", "Windows Chrome 122"]
        while self.is_active:
            time.sleep(random.uniform(0.1, 0.4))
            u = f"{self.platform_tag}_{random.randint(100, 9999)}"
            info = f"Agent: {random.choice(agents)} | Status: 200"
            Clock.schedule_once(lambda dt, user=u, inf=info: self.log(user, inf))

    def log(self, u, inf):
        if self.is_active:
            self.ids.log_stream.text += f"\n[+] TRACE >> {u} | {inf}"
            self.ids.scroll_view.scroll_y = 0
            if random.random() > 0.994:
                HITS_ARCHIVE[self.platform_tag].append(u)
                Snackbar(text=f"🎯 {self.platform_tag} HIT SAVED!", bg_color=(0, 0.4, 0, 1)).open()
                if platform == 'android':
                    try:
                        from jnius import autoclass
                        v = autoclass('org.kivy.android.PythonActivity').mActivity.getSystemService('vibrator')
                        v.vibrate(100)
                    except: pass

class AbdoDemonUltimate(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    def open_classified_archive(self):
        summary = ""
        for tag, hits in HITS_ARCHIVE.items():
            if hits: summary += f"--- {tag} --- \\n" + "\\n".join(hits[-5:]) + "\\n"
        txt = summary if summary else "Archive Empty."
        instruct = fix_ar("\\n\\n--- تعليمات السحب ---\\n1. انسخ المعرف\\n2. استخدم تخطي V33")
        self.dialog = MDDialog(
            title="📜 ROYAL ARCHIVE",
            text=f"{txt}{instruct}",
            buttons=[
                MDFlatButton(text="CLEAR", on_release=self.clear_hits),
                MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()
    def clear_hits(self, *args):
        for k in HITS_ARCHIVE: HITS_ARCHIVE[k] = []
        if self.dialog: self.dialog.dismiss()
        Snackbar(text="تم تطهير الأرشيف الملكي").open()

if __name__ == "__main__":
    AbdoDemonUltimate().run()