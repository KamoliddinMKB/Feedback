from telegram.ext import Updater,MessageHandler,ConversationHandler,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram.update import Update
import logging
from telegram import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
import time
from telegram import Bot
#logging.basicConfig(
#    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
#    level=logging.DEBUG
#)

updater:Updater=Updater(token='1977706812:AAF3Hdg2eAxjJs9aSdYQR41HzD8wxt_XPGg')
dispatcher=updater.dispatcher

MENU_STATE=0
PASSWORD_STATE=1
ADMIN_STATE=2
CHANGE_STATE=3
CHANGE_PASSWORD_STATE=4

def start_handler(update:Update,context:CallbackContext):
    update.message.reply_text("Salom!!!\nBu Muhiddinov Kamoliddin tomonidan tayyorlangan dars jadval bot!!!\n"
                              "\nEslatib o'tishim darkor, bu bot hech qanday reklama roliklarini yoki telegram guruhlar;kanallar;botlar linklarini yubormaydi!!!"
                              "\nDars jadvalini ko'rish uchun /menu buyrug'ini kiriting."
                              "\nAdmin panelga o'tish uchun /admin buyrug'ini kiriting."
                              "\nAgar biror muammo tug'ilsa "
                              "t.me/kamoliddinmuhiddinov ga murojaat qiling.")
    return MENU_STATE

def menu_handler(update:Update,context:CallbackContext):
    reply_keyboard=[[KeyboardButton("Dushanba_001"),KeyboardButton("Seshanba_002"),KeyboardButton("Chorshanba_003")],
                    [KeyboardButton("Payshanba_004"),KeyboardButton("Juma_005"),KeyboardButton("Shanba_006")],[KeyboardButton("Admin_Panel")],]
    update.message.reply_text("Pastdagilardan birini tanlang:",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True,one_time_keyboard=True))

def mon(update:Update,context:CallbackContext):
    with open('dush.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr)==4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr)==3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr)==2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr)==5:
            a = satr[0]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def tue(update:Update,context:CallbackContext):
    with open('sesh.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr)==4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr)==3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr)==2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr)==5:
            a = satr[0]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def wed(update:Update,context:CallbackContext):
    with open('chor.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def thu(update:Update,context:CallbackContext):
    with open('pay.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def fri(update:Update,context:CallbackContext):
    with open('juma.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def sat(update:Update,context:CallbackContext):
    with open('shan.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def exit_to_admin(update:Update,context:CallbackContext):
    update.message.reply_text("Siz hozir admin panelga kirishda turibsiz! Admin panelga kirish uchun kodni kiritishingiz kerak!\n/code dan so'ng kodni kiriting\nMasalan:/code 123\nChiqish uchun /menu buyrug'ini kiriting!!!")
    return PASSWORD_STATE

def sett(update:Update,context:CallbackContext):
    reply_keyboard=[[KeyboardButton("Fanlarni o'zgartirish"),KeyboardButton("Admin panel parolini almashtirish")],[KeyboardButton("Admin paneldan chiqish"),KeyboardButton("Hamma fanlar")]]
    update.message.reply_text("Pastdagilardan birini tanlang",reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True,one_time_keyboard=True))

def code(update:Update,context:CallbackContext):
    with open('users.txt','r') as pas:
        pw=pas.readline()
        args = context.args
        code = ''.join(args)
        if code==pw:
            update.message.reply_text("Siz admin saytga kirish huquqiga ega bo'ldingiz!!!\nEndi /set buyrug'i asosida admin panelga o'ting.")
            return ADMIN_STATE
        else:
            update.message.reply_text("Siz admin panelga kirish parolini xato terdingiz!!!\nEndi avtomatik ravishda asosiy menyuga qaytarilasiz!!!\nMenuni yoqish uchun /menu buyrug'ini kiriting")
            return MENU_STATE

def change(update:Update,context:CallbackContext):
    reply_keyboard = [[KeyboardButton("Dushanba_001"), KeyboardButton("Seshanba_002"),KeyboardButton("Chorshanba_003")],
                      [KeyboardButton("Payshanba_004"), KeyboardButton("Juma_005"), KeyboardButton("Shanba_006")],[KeyboardButton("Admin panel asosiy sahifasiga qaytish")]]
    update.message.reply_text("Pastdagilardan birini tanlang:",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                                               one_time_keyboard=True))

def ch_mon(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /monday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/monday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_tu(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /tuesday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/tuesday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_w(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /wednesday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/wedday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_th(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /thursday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/thursday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_f(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /friday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/friday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_s(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /saturday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/saturday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def changem(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('dush.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Dushanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /monday buyrug'i asosida qayta kiriting\nMasalan:\n/monday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('dush.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Dushanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /monday buyrug'i asosida qayta kiriting\nMasalan:\n/monday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('dush.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Dushanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /monday buyrug'i asosida qayta kiriting\nMasalan:\n/monday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /monday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def changetu(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('sesh.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Seshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /tuesday buyrug'i asosida qayta kiriting\nMasalan:\n/tuesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('sesh.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Seshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /tuesday buyrug'i asosida qayta kiriting\nMasalan:\n/tuesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('sesh.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Seshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /tuesday buyrug'i asosida qayta kiriting\nMasalan:\n/tuesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /tuesday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def changew(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('chor.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Chorshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /wednesday buyrug'i asosida qayta kiriting\nMasalan:\n/wednesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('chor.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Chorshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /wednesday buyrug'i asosida qayta kiriting\nMasalan:\n/wednesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('chor.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Chorshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /wednesday buyrug'i asosida qayta kiriting\nMasalan:\n/wednesday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /wednesday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def changeth(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('pay.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Payshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /thursday buyrug'i asosida qayta kiriting\nMasalan:\n/thursday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('pay.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Payshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /thursday buyrug'i asosida qayta kiriting\nMasalan:\n/thursday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('pay.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Payshanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /thursday buyrug'i asosida qayta kiriting\nMasalan:\n/thursday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /thursday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def changef(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('juma.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Juma kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /friday buyrug'i asosida qayta kiriting\nMasalan:\n/friday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('juma.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Juma kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /friday buyrug'i asosida qayta kiriting\nMasalan:\n/friday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('juma.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Juma kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /friday buyrug'i asosida qayta kiriting\nMasalan:\n/friday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /friday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def changes(update:Update,context:CallbackContext):
    args=context.args
    if len(args)==7:
        a=args[0]
        b=args[1]
        c=args[2]
        d=args[3]
        e=args[4]
        f=args[5]
        g=args[6]
        with open('shan.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}')
        update.message.reply_text("Shanba kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /saturday buyrug'i asosida qayta kiriting\nMasalan:\n/saturday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==6:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        f = args[5]
        with open('shan.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
        update.message.reply_text("Juma kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /saturday buyrug'i asosida qayta kiriting\nMasalan:\n/saturday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    elif len(args)==5:
        a = args[0]
        b = args[1]
        c = args[2]
        d = args[3]
        e = args[4]
        with open('shan.txt','w') as dush:
            dush.write(f'{a}\n{b}\n{c}\n{d}\n{e}')
        update.message.reply_text("Juma kungi yangi jadval saqlandi!!!\nAgar xato kiritgan bo'lsangiz /saturday buyrug'i asosida qayta kiriting\nMasalan:\n/saturday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",
                                  reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    else:
        update.message.reply_text(
            "Siz kiritgan darslar soni 5 tadan kam yoki 7 tadan ko'p.\n Iltimos /saturday buyrug'i asosida fanlarni qayta kiriting yoki pastdagilardan birini bosing.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Admin panelning bosh sahifasiga o'tish"), KeyboardButton("Menyu panelga qaytish")]],
                resize_keyboard=True))

def setta(update:Update,context:CallbackContext):
    update.message.reply_text("Siz admin panelni bosh sahifasida turibsiz\nAdmin panelni ichiga kirish uchun /set buyrug'ini kiriting.")
    return ADMIN_STATE

def exit_m(update:Update,context:CallbackContext):
    update.message.reply_text("Siz asosiy menyuga qaytdingiz\nMenyuni /menu buyrug'i asosida faollashtiring!")
    return MENU_STATE

def ch_p(update:Update,context:CallbackContext):
    update.message.reply_text("/code buyrug'idan keyin yangi parolni kiriting\n UNUTMANG,PAROLDA   :;\|*/-+()!~#$%^&<>?   SIMVOLLARI ISHTIROK ETMASLIGI LOZIM!!!\nOrqaga qaytish uchun /back buyrug'ini kiriting.")
    return CHANGE_PASSWORD_STATE

def MKB(update:Update,context:CallbackContext):
    with open('users.txt','r') as fayl:
        satr=fayl.readline()
        update.message.reply_text(satr+"\nAdmin panelga xush kelibsiz, Kamoliddin Muhiddinov\n Admin saytni /set buyrug'i asosida faollashtirishingiz mumkin")
        return ADMIN_STATE

def exit_menu(update:Update,context:CallbackContext):
    update.message.reply_text("Siz menu panelga qaytdingiz!\nMenyuni /menu buyrug'i asosida faollashtiring!")
    return MENU_STATE

def ch_pas(update:Update,context:CallbackContext):
    args=context.args
    code=''.join(args)
    with open('users.txt','w') as fayl:
        fayl.write(code)
    reply_keyboard = [[KeyboardButton("Menyu panelga qaytish"), KeyboardButton("Admin sayt bosh sahifasiga o'tish")]]
    update.message.reply_text("Parol muvaffaqqiyatli almashtirildi.\nAgar parolni xato kiritgan bo'lsangiz,/code buyrug'idan so'ng parolni yozishingiz mumkin yoki pastdagilardan birini tanlang",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True,one_time_keyboard=True))

def menu_handler_admin(update:Update,context:CallbackContext):
    update.message.reply_text("Siz menyu panelga qaytdingiz. Menyuni /menu buyrug'i asosida faollashtiring.")
    return MENU_STATE

def all(Update,CallbackContext):
    mon(Update,CallbackContext)
    tue(Update,CallbackContext)
    wed(Update,CallbackContext)
    thu(Update,CallbackContext)
    fri(Update,CallbackContext)
    sat(Update,CallbackContext)

def about(update:Update,context:CallbackContext):
    update.message.reply_text(  )

def uxla(update:Update,context:CallbackContext):
    update.message.reply_text("Hammaga xayr, salomat bo'ling!")

dispatcher.add_handler(ConversationHandler(
    entry_points=[
        CommandHandler('start',start_handler),
        CommandHandler('admin',exit_to_admin),
        CommandHandler('menu',menu_handler),
        MessageHandler(Filters.regex(r'Dushanba_001'),mon),
        MessageHandler(Filters.regex(r'Seshanba_002'),tue),
        MessageHandler(Filters.regex(r'Chorshanba_003'),wed),
        MessageHandler(Filters.regex(r'Payshanba_004'),thu),
        MessageHandler(Filters.regex(r'Juma_005'),fri),
        MessageHandler(Filters.regex(r'Shanba_006'),sat),
        MessageHandler(Filters.regex(r'Admin_Panel'),exit_to_admin),
        MessageHandler(Filters.regex(r"MKB admin"),MKB),
        MessageHandler(Filters.regex(r"Uyqu rejimi"),uxla),

        CommandHandler('dushanba001',mon),
        CommandHandler('seshanba002',tue),
        CommandHandler('chorshanba003',wed),
        CommandHandler('payshanba004',thu),
        CommandHandler('juma005',fri),
        CommandHandler('shanba006',sat),
        CommandHandler('jadval',all),
        CommandHandler('about',about)

    ],
    states={
        MENU_STATE:[
            CommandHandler('admin',exit_to_admin),
            CommandHandler('menu',menu_handler),
            MessageHandler(Filters.regex(r'Dushanba_001'),mon),
            MessageHandler(Filters.regex(r'Seshanba_002'),tue),
            MessageHandler(Filters.regex(r'Chorshanba_003'),wed),
            MessageHandler(Filters.regex(r'Payshanba_004'),thu),
            MessageHandler(Filters.regex(r'Juma_005'),fri),
            MessageHandler(Filters.regex(r'Shanba_006'),sat),
            MessageHandler(Filters.regex(r'Admin_Panel'),exit_to_admin),
            MessageHandler(Filters.regex(r"MKB admin"),MKB),

            CommandHandler('start',start_handler),
            CommandHandler('dushanba001',mon),
            CommandHandler('seshanba002',tue),
            CommandHandler('chorshanba003',wed),
            CommandHandler('payshanba004',thu),
            CommandHandler('juma005',fri),
            CommandHandler('shanba006',sat),
            CommandHandler('jadval',all),
            ],
        PASSWORD_STATE:[
            CommandHandler('code',code),
            CommandHandler('start',start_handler),
            CommandHandler('menu',menu_handler_admin),
        ],
        ADMIN_STATE:[
            CommandHandler('set',sett),
            MessageHandler(Filters.regex(r"Fanlarni o'zgartirish"),change),
            MessageHandler(Filters.regex(r"Admin panel parolini almashtirish"),ch_p),
            MessageHandler(Filters.regex(r"Admin paneldan chiqish"),exit_menu),
            MessageHandler(Filters.regex(r'Dushanba_001'),ch_mon),
            MessageHandler(Filters.regex(r'Seshanba_002'),ch_tu),
            MessageHandler(Filters.regex(r'Chorshanba_003'),ch_w),
            MessageHandler(Filters.regex(r'Payshanba_004'),ch_th),
            MessageHandler(Filters.regex(r'Juma_005'),ch_f),
            MessageHandler(Filters.regex(r'Shanba_006'),ch_s),
            MessageHandler(Filters.regex(r"Admin panel asosiy sahifasiga qaytish"),setta),
            CommandHandler('start',start_handler),
            MessageHandler(Filters.regex(r"Hamma fanlar"),all)
        ],
        CHANGE_STATE:[
            CommandHandler('monday', changem),
            CommandHandler('tuesday', changetu),
            CommandHandler('wednesday', changew),
            CommandHandler('thursday', changeth),
            CommandHandler('friday', changef),
            CommandHandler('saturday', changes),
            MessageHandler(Filters.regex(r"Admin panelning bosh sahifasiga o'tish"),setta),
            MessageHandler(Filters.regex("Menyu panelga qaytish"),exit_m),
            CommandHandler('start',start_handler),

        ],
        CHANGE_PASSWORD_STATE:[
            CommandHandler('code',ch_pas),
            MessageHandler(Filters.regex(r'Menyu panelga qaytish'),exit_m),
            MessageHandler(Filters.regex(r"Admin sayt bosh sahifasiga o'tish"),setta),
            CommandHandler('back',setta),
            CommandHandler('start',start_handler),
        ]
                },
    fallbacks=[]
))
updater.start_polling()
updater.idle()