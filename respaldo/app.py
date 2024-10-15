from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plato/<nombre>')
def plato(nombre):
    descripciones = {
        'quinoa': 'La quinoa es una excelente fuente de proteínas y fibra, ideal para una alimentación equilibrada. Esta ensalada de quinoa es nutritiva y versátil, ya que puedes añadir tus ingredientes preferidos.',
        'pollo': 'La técnica de la plancha permite que las pechugas de pollo se cocinen de manera uniforme, lo que resulta en una carne jugosa y tierna.',
        'fruta': 'Plato de fruta fresca de temporada.',
        'crema_verduras': 'Las cremas de verduras son una forma perfecta de aumentar la ingesta de verduras en nuestra alimentación diaria. Las verduras son una fuente rica en vitaminas, minerales y fibra, y consumirlas en forma de cremas nos permite obtener todos sus nutrientes de una manera fácil de consumir.',
        'pescado': 'Esta receta de Pescado al horno tiene un método de cocción mantiene la jugosidad del pescado, mientras que el limón y el romero le añaden un toque de frescura y aroma inigualables.',
        'fideos_salsa':'Tradicional preparación italiana de pasta armónicamente acompañada de nuestra exquisita salsa boloñesa. Elaborada con la mejor carne picada y salsa de tomates de primera calidad. Un plato delicioso y abundante, con el sabor inconfundible de nuestras recetas caseras.',
        'ensalada_atun':'La ensalada de atún es un platillo fresco que combina atún con verduras como lechuga, pepino y tomate, y se adereza con mayonesa o vinagreta. Se puede servir sola o en sándwiches, ideal para comidas ligeras y rápidas.',
       'garbanzos':'Los garbanzos son legumbres de sabor suave y textura firme, ricos en proteínas y fibra. Se usan en ensaladas, guisos y purés como el hummus.',
       'tortilla_espinacas':'Las tortillas de espinaca son tortillas que incorporan espinacas cocidas, lo que les da un color verde y un sabor suave. Se pueden usar en tacos, burritos y quesadillas, aportando un toque nutritivo y atractivo a los platos.',
       'gelatina':'La gelatina es un postre hecho de colágeno que tiene una textura suave y gelatinosa. Se presenta en varios colores y sabores, y se utiliza en postres, mousses y para dar consistencia a salsas. Es baja en calorías y no contiene grasa.',
       'ensalada_tomate':'La ensalada de tomate es un plato fresco que combina rodajas de tomate con ingredientes como cebolla, albahaca y aderezo de aceite de oliva y vinagre. Es sencilla y resalta el sabor natural del tomate.',
       "pescado_empanizado":"El pescado empanizado es un filete cubierto con pan rallado o harina y luego frito o horneado, logrando una textura crujiente por fuera y jugosa por dentro. Se suele acompañar con limón y salsas",
       "caldo_res":"El caldo de res es una sopa hecha con carne de res, huesos y verduras como zanahoria, papa y calabacita. Tiene un sabor reconfortante y se sirve caliente, ideal para días fríos.",
       "arroz_frijoles":"El arroz con frijoles es un platillo tradicional que mezcla arroz y frijoles cocidos con especias, ideal como acompañamiento o plato principal en la cocina latinoamericana.",
       "chili_carne":"El chili con carne es un guiso picante hecho con carne molida, frijoles, tomate y especias como comino y chile. Es popular en la cocina tex-mex y se sirve con tortillas o pan.",
       "pasta_verduras":"La pasta con verduras es un platillo que combina pasta cocida con vegetales salteados como brócoli, zanahoria y pimientos, y se adereza con hierbas y aceite de oliva. Es ligero y nutritivo.",
       "ensalada_verde":"La ensalada verde es un platillo fresco que mezcla lechuga, espinaca y otras hojas verdes, a menudo acompañadas de pepino, aguacate y aderezo ligero. Ideal como guarnición o entrada.",
       "sopa_fideos":"La sopa de fideos es un caldo caliente con fideos cocidos y, a veces, verduras. Es sencilla, reconfortante y popular en muchas cocinas como entrada o plato principal.",
       "ensalada_pollo":"La ensalada de pollo es un plato que mezcla trozos de pollo con verduras como lechuga, tomate y zanahoria. Se adereza con mayonesa, yogurt o vinagreta, y se sirve fría como plato principal o acompañamiento.",
       "helado":"El helado es un postre congelado cremoso hecho a base de leche, crema, azúcar y saborizantes como frutas o chocolate. Es popular en diversas variedades y se sirve en conos, copas o como acompañamiento de otros postres.",
       "sopa_verduras":"La sopa de verduras es un caldo caliente que mezcla diversos vegetales, como zanahorias y papas, sazonado con hierbas. Es nutritiva y reconfortante, ideal como entrada o comida ligera.",
       "caldo_res":"El caldo de res es una sopa hecha con carne de res, huesos y verduras, que se cocina a fuego lento para extraer su sabor. Es reconfortante y se sirve caliente, ideal para días fríos.",
       "ensalada_rusa":"La ensalada rusa es un platillo frío que combina papas, zanahorias, guisantes y mayonesa. A menudo incluye ingredientes adicionales como huevo duro y aceitunas, y se sirve como entrada o acompañamiento.",
       "pure_papa":"El puré de papa es un acompañamiento cremoso hecho de papas cocidas y trituradas, mezcladas con mantequilla, leche y sal. Es suave y se sirve comúnmente junto a carnes y guisos.",
       "hamburguesa":"La hamburguesa es un sándwich que consiste en una carne molida (generalmente de res) cocinada, colocada entre dos panes y a menudo acompañada de lechuga, tomate, cebolla, queso y salsas. Es un platillo popular en la comida rápida.",
       "verduras_salteadas":"Las verduras salteadas son vegetales cocinados rápidamente en una sartén con un poco de aceite, a menudo sazonados con hierbas y especias. Son un acompañamiento saludable y colorido, ideal para resaltar el sabor natural de los vegetales.",
       "gazpacho":"El gazpacho es una sopa fría española hecha a base de tomates, pimientos, pepinos, cebolla y ajo, todo triturado y sazonado con aceite de oliva, vinagre y sal. Es refrescante y ideal para los días calurosos.",
       "pollo_curry":"El pollo al curry es un platillo que consiste en trozos de pollo cocidos en una salsa de curry, que puede incluir ingredientes como leche de coco, cebolla, ajo y especias. Es sabroso y aromático, y se sirve comúnmente con arroz.",
       "flan":"El flan es un postre cremoso de origen español hecho a base de huevos, leche y azúcar, con una capa de caramelo en la parte superior. Es suave y dulce, y se sirve frío.",
       "carne_horno":"La carne al horno es un platillo que consiste en trozos de carne, como res, cerdo o pollo, cocinados en el horno con especias y marinados. Se caracteriza por su sabor jugoso y tierno, y se suele acompañar de verduras asadas o puré.",
       "arroz_pollo":"El arroz con pollo es un plato tradicional que combina arroz cocido con trozos de pollo, verduras y especias. Es popular en muchas culturas y tiene diversas variaciones según la región.",
       "sopa_pollo":"La sopa de pollo es un platillo reconfortante hecho con caldo de pollo, vegetales, fideos o arroz, y especias. Es ligera, nutritiva y a menudo se sirve para reconfortar en climas fríos o cuando se necesita una comida reconfortante.",
       "pasta_pesto":"La pasta al pesto es un plato italiano clásico que consiste en pasta mezclada con una salsa de pesto hecha de albahaca, ajo, piñones, queso parmesano y aceite de oliva. Es fresca, aromática y fácil de preparar.",
       "arroz_integral":"El arroz integral es una variedad de arroz que conserva su cáscara y salvado, lo que le aporta más fibra, nutrientes y un sabor ligeramente más a nuez que el arroz blanco. Es una opción saludable y versátil en muchas recetas.",
       "tortilla_espanola":"La tortilla española es un platillo tradicional de España hecho con huevos, papas y, a menudo, cebolla. Se cocina lentamente en una sartén hasta obtener una textura suave y jugosa. Es ideal como aperitivo, plato principal o tapa.",
       "carne_molida":"La carne molida es carne de res desmenuzada y triturada, utilizada como base en una gran variedad de recetas como hamburguesas, tacos, albóndigas y salsas. Es versátil y se adapta fácilmente a diferentes preparaciones y sazones.",
       "pizza":"La pizza es un platillo originario de Italia, que consiste en una base de masa cubierta con salsa de tomate, queso y diversos ingredientes como verduras, carnes y especias. Se hornea hasta que la masa está crujiente y el queso se derrite, ofreciendo una combinación de sabores y texturas.",
       "ensalada_cesar":"La ensalada César es una ensalada clásica que combina lechuga romana, crutones, queso parmesano y aderezo César, que se elabora con ingredientes como yema de huevo, ajo, mostaza y aceite de oliva. Es fresca, sabrosa y a menudo se acompaña de pollo a la parrilla.",
       "yogur":"El yogurt es un producto lácteo cremoso que resulta de la fermentación de la leche con cultivos bacterianos. Es conocido por su textura suave y sabor ligeramente ácido, además de ser rico en proteínas, calcio y probióticos, lo que lo convierte en un alimento saludable y versátil para consumir solo o en recetas.",
       "lentejas_estofadas":"Las lentejas estofadas son un plato nutritivo y reconfortante que consiste en lentejas cocidas lentamente con verduras, especias y, a menudo, carne o chorizo. Este guiso es rico en proteínas, fibra y sabor, ideal para los días fríos.",
       "pasta_salsa":"La pasta con salsa es un platillo versátil que consiste en fideos de pasta cocidos y acompañados de una variedad de salsas, como marinara, pesto, alfredo o boloñesa. Es fácil de preparar, sabrosa y se puede personalizar con ingredientes como verduras, carne o queso.",
       "pollo_horno":"El pollo al horno es un platillo delicioso y jugoso que se prepara asando un pollo entero o sus piezas en el horno, a menudo sazonado con hierbas, especias y acompañamientos como verduras. Es una opción popular para comidas familiares y celebraciones.",
       "pescado_plancha":"El pescado a la plancha es un platillo saludable que consiste en filetes de pescado cocinados a la parrilla o en una sartén caliente con poco aceite. Se caracteriza por su textura tierna y su sabor fresco, y a menudo se sirve con limón, hierbas o acompañamientos como ensaladas o verduras.",
       "tacos_carne":"Los tacos de carne son un platillo tradicional mexicano que consiste en tortillas de maíz o harina rellenas de carne asada, carne molida, carnitas u otras variedades de carne, acompañados de cebolla, cilantro, salsa y a veces aguacate. Son sabrosos, versátiles y perfectos para compartir.",
       "arroz_frito":"El arroz frito es un platillo popular en muchas cocinas asiáticas, hecho con arroz cocido salteado en un wok con verduras, proteínas como pollo, cerdo o camarones, y sazonado con salsa de soja y especias. Es un plato sabroso y fácil de preparar, ideal para aprovechar sobras de arroz.",
       "carne_asada":"La carne asada es un platillo mexicano que consiste en carne de res marinada y asada a la parrilla, generalmente acompañada de cebollas, chiles y cilantro. Se sirve en tacos, burritos o como plato principal, y es conocida por su sabor ahumado y jugoso.",
       "filete_ternera":"El filete de ternera es un corte tierno y jugoso de carne de res, ideal para cocinar a la parrilla, a la plancha o al horno. Su sabor suave y su textura delicada lo convierten en una opción popular en platos gourmet y cenas elegantes. Se puede servir con salsas, guarniciones o simplemente sazonado con sal y pimienta.",
       "wrap_pollo":"El wrap de pollo es un platillo que consiste en pollo sazonado y cocido, envuelto en una tortilla de harina o integral con verduras frescas, salsas y otros ingredientes. Es una opción deliciosa y práctica para disfrutar en cualquier momento.",
       "quiche":"El quiche es un tipo de tarta salada de origen francés, hecha con una base de masa y un relleno a base de huevos, crema y queso, junto con diversos ingredientes como verduras, carnes o mariscos. Se sirve caliente o fría y es ideal como aperitivo o plato principal.",















    }
    
    # Crear un objeto plato con los atributos necesarios
    plato_info = {
        'nombre': nombre,
        'descripcion': descripciones.get(nombre, "Descripción no disponible."),
        'link': 'https://ejemplo.com'  # Puedes cambiar esto por un enlace relevante
    }
    
    return render_template('plato.html', plato=plato_info)

if __name__ == '__main__':
    app.run(debug=True)
