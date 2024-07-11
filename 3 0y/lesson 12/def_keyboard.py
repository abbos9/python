from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='®️ Regist'),
            KeyboardButton(text='👤 profile')

        ]
    ], resize_keyboard=True

)


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍴 Menyu')
        ],
        [
            KeyboardButton(text='🛍 Mening buyurtmalarim')
        ],
        [
            KeyboardButton(text='✍️ Fikr bildirish'),
            KeyboardButton(text='⚙️ Sozlamalar')
        ]
    ], resize_keyboard=True
)
products_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🫔 Lavash'),
            KeyboardButton(text='🌮 Trindwich'),
        ],
        [
            KeyboardButton(text='🍲 Shaurma'),
            KeyboardButton(text='🍔 Burger'),
        ],
        [
            KeyboardButton(text='Sub'),
            KeyboardButton(text='Kartoshka'),
        ],

        [KeyboardButton(text='Hot-Dog'),
         KeyboardButton(text='Sneklar'),
         ],

        [
            KeyboardButton(text='Salat, garnir, non'),
            KeyboardButton(text='souslar'),
        ],
        [
            KeyboardButton(text='Setlar'),
            KeyboardButton(text='Desertlar'),
        ],
        [
            KeyboardButton(text='Issiq ichimliklar'),
            KeyboardButton(text='Sovuq ichimliklar'),
        ],

        [
            KeyboardButton(text='📥 Savat'),
            KeyboardButton(text='⬅️ mahsulotlar')
        ]
    ], resize_keyboard=True
)
lavash_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tovuq go`shtidan lavash'),
            KeyboardButton(text="Mol go'shtidan pishloqli lavash")
        ],
        [
            KeyboardButton(text="Mol go'shtidan qalampir lavash"),
            KeyboardButton(text="Tovuq go'shtidan qalampir lavash"),
        ],
        [
            KeyboardButton(text='Tovuq go`shtidan pishloqli lavash'),
            KeyboardButton(text='Fitter')
        ],
        [
            KeyboardButton(text='Mol go`shtidan lavash'),
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
shaurma_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mol go'shtidan qalampir shaurma"),
            KeyboardButton(text="Tovuq go'shtidan shaurma")
        ],
        [
            KeyboardButton(text="Tovuq go'shtidan qalampir shaurma"),
            KeyboardButton(text="Mol go'shtidan shaurma"),
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
trindvich_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🐓 Tovuq go`shtidan trindvich'),
            KeyboardButton(text='🐄 Mol go`shtidan trindvich')
        ],
        [
            KeyboardButton(text='⬅️ Mahsulotlar')
        ]
    ], resize_keyboard=True
)
burger_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gamburger"),
            KeyboardButton(text="Dablburger")
        ],
        [
            KeyboardButton(text="Chizburger"),
            KeyboardButton(text="dablchizburger"),
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Sub_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tovuq go`shtidan sab"),
            KeyboardButton(text="Tovuq go`shtidan pishloqli sab")
        ],
        [
            KeyboardButton(text="Mol go`shtidan pishloqli sab"),
            KeyboardButton(text="Mol go`shtidan sab"),
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Kartoshka_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Jaydari kartoshka"),
            KeyboardButton(text="kartoshka fri")
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Hot_Dog_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="hot-dog"),
            KeyboardButton(text="hot-dog_dabl")
        ],
        [
            KeyboardButton(text="Bolalar uchun Hot-Dog"),
            KeyboardButton(text="hot-dog-mini"),
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Sneklar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="smaylik"),
            KeyboardButton(text="strips")
        ],

        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Salat_garnir_non_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="guruch"),
            KeyboardButton(text="non")
        ],
        [
            KeyboardButton(text="salat"),
            KeyboardButton(text="sezer salat"),
        ],
        [
            KeyboardButton(text='gercheksiy salat')
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
souslar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='sezar sous'),
            KeyboardButton(text='nordon shirin')
        ],
        [
            KeyboardButton(text='gercheskiy sous'),
            KeyboardButton(text='tomatli ketchup')
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
Setlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="combo plus"),
            KeyboardButton(text="combo plus isituvchan(kok choy)")
        ],
        [
            KeyboardButton(text="Mol go'shtidan donar"),
            KeyboardButton(text="FitCombo"),
        ],
        [
            KeyboardButton(text="Tovuq go'shtidan donar"),
            KeyboardButton(text="COMBO PLUS isituvchan (qora choy)")
        ],
        [
            KeyboardButton(text="Bolalar uchun Combo"),
            KeyboardButton(text="Donar-box tovuq go'shtli")
        ],
        [
            KeyboardButton(text="Donar-box mol go'shtli")
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
desert_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="karamel donut"),
            KeyboardButton(text="medovik"),
        ],
        [
            KeyboardButton(text="chizkeyk"),
            KeyboardButton(text="mevali donut"),
        ], [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ], resize_keyboard=True
)
