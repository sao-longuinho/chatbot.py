import math
import difflib

def character_distance(texto_a, texto_b):
    similaridade = difflib.SequenceMatcher(None, texto_a, texto_b).ratio() 
    
    return 1 - similaridade 

dataset = [ ("O que são os indígenas?",
     "Os indígenas são os povos originários de uma determinada região, ou seja, são os primeiros habitantes de um território antes da chegada de colonizadores ou de outras populações externas. No caso das Américas, os indígenas já viviam nessas terras milhares de anos antes da chegada dos europeus no século XV."),

    ("O que são aldeias indígenas?",
     "Aldeias indígenas são comunidades onde povos originários vivem de acordo com suas tradições, mantendo sua cultura, espiritualidade e ligação com a terra. Elas reúnem atividades como agricultura, rituais e artesanato, e são essenciais para preservar e transmitir saberes ancestrais."),

    ("Por que não chamar os indígenas de índio?",
     "O termo índio é inadequado por ter origem em um equívoco histórico e por generalizar diversos povos com culturas, línguas e identidades distintas. O mais apropriado é utilizar indígenas, pois reconhece esses grupos como os povos originários do território e respeita sua diversidade e especificidade cultural."),

    ("No Vale do Paranhana há quantas aldeias?",
     "Atualmente, não há uma fonte segura que informe com certeza quantas aldeias indígenas há no Vale do Paranhana. Contudo, é importante destacar que o estado do Rio Grande do Sul abriga diversas comunidades indígenas, principalmente dos povos Kaingang, Mbya-Guarani, Xokleng e Charrua. Esses grupos estão distribuídos em várias regiões, incluindo áreas próximas ao Vale do Paranhana."),

    ("Quais são as aldeias no Vale do Paranhana?",
     "Atualmente, não há informações públicas detalhadas sobre o número exato de aldeias indígenas localizadas no Vale do Paranhana."),

    ("Por que não se referir às aldeias como tribos?",
     "Não se deve chamar as aldeias indígenas de tribos porque esse termo é genérico e muitas vezes carregado de uma visão colonial e simplista, que não respeita a complexidade cultural e social dos povos indígenas. Tribo costuma agrupar diversos grupos distintos, apagando suas identidades específicas, enquanto aldeia se refere a uma comunidade concreta, com sua própria organização, costumes e território. Usar aldeia valoriza a diversidade e a autonomia desses povos."),

    ("Como é a hierarquia em uma aldeia indígena?",
     "A hierarquia em uma aldeia indígena varia conforme o povo, mas geralmente existe uma liderança baseada em respeito, tradição e consenso. Normalmente, há um cacique ou líder escolhido pela comunidade, que representa o grupo, toma decisões importantes e cuida da relação com o exterior. Além do cacique, podem existir anciãos ou conselheiros que ajudam na tomada de decisões e na resolução de conflitos. A organização é mais coletiva, valorizando o diálogo e a participação de todos, em vez de um poder centralizado rígido."),

    ("Quais funções cada indígena exerce?",
     "Dentro de uma aldeia indígena, as funções de cada pessoa variam conforme a cultura do povo, mas geralmente existem alguns papéis comuns. O cacique atua como líder, representando a aldeia, tomando decisões importantes e cuidando das relações com outras comunidades e o mundo externo. Os anciãos são responsáveis por guardar os saberes, histórias, tradições e rituais, além de orientar os mais jovens. Os guerreiros protegem a aldeia e seu território, enquanto os xamãs ou pajés cuidam da saúde espiritual e física da comunidade, realizando rituais e curas. Caçadores, pescadores e agricultores garantem o alimento para todos. Os artesãos produzem utensílios, ferramentas, roupas e objetos de arte. As mulheres, além de participarem de várias dessas funções, geralmente cuidam da preparação da comida, do cuidado das crianças e da transmissão cultural. Todas essas funções são valorizadas e essenciais para o equilíbrio e bem-estar da aldeia."),

    ("Qual o intuito das tatuagens ou pinturas corporais? Como elas são chamadas?",
     "As tatuagens e pinturas corporais indígenas, muitas vezes chamadas de pinturas corporais ou corpo-pintado, têm o intuito de expressar a identidade cultural, social e espiritual do indivíduo e do grupo. Elas servem para marcar rituais importantes, como iniciações, cerimônias, festas e guerras, além de simbolizar a pertença a um determinado povo, clã ou função dentro da aldeia. Essas pinturas também podem proteger espiritualmente, transmitir mensagens e representar a conexão com a natureza e os ancestrais. Cada desenho, cor e formato tem um significado específico que varia entre os diferentes povos indígenas."),

    ("Como fazem seus armamentos?",
     "Os indígenas fabricam seus armamentos tradicionais usando materiais naturais da região, como madeira, pedra, osso e fibras vegetais. Arcos e flechas são comuns, com pontas feitas de pedra ou osso, às vezes envenenadas para caça. Também usam zarabatanas, lanças e boleadeiras. Essas armas são feitas com técnicas passadas de geração em geração, adaptadas ao ambiente e às necessidades do grupo. Hoje, alguns povos combinam esses métodos com materiais modernos para garantir sua defesa."),

    ("Como são passados os ensinamentos medicinais?",
     "Os ensinamentos medicinais indígenas são transmitidos principalmente de forma oral, de geração em geração, por meio de histórias, rituais e práticas tradicionais. Os mais experientes, como os xamãs ou pajés, ensinam sobre plantas medicinais, tratamentos e curas, compartilhando conhecimentos sobre a relação entre o corpo, a natureza e o espiritual. Esse aprendizado acontece dentro da comunidade, acompanhando os rituais e o cotidiano, preservando saberes ancestrais."),

    ("Como é o calendário ou datas importantes para os povos indígenas?",
     "O calendário dos povos indígenas está ligado aos ciclos da natureza, como o sol, a lua, as estações e os movimentos dos animais e plantas. As datas importantes geralmente são marcadas por eventos naturais, como períodos de plantio, colheita, migração de animais ou mudanças climáticas. Além disso, há festivais, rituais e celebrações que comemoram a conexão com os ancestrais, a espiritualidade, as conquistas do grupo e momentos de renovação. Essas datas variam bastante entre os diferentes povos, refletindo suas culturas e ambientes específicos."),

    ("Existem danças tradicionais? O que elas representam?",
     "Os povos indígenas têm muitas danças tradicionais que são muito importantes para sua cultura. Essas danças geralmente representam histórias, rituais, celebrações, conexões com a natureza e com os ancestrais. Elas podem marcar momentos como festas, ritos de passagem, agradecimentos, pedidos de proteção ou boas colheitas. Cada povo tem seus próprios estilos, ritmos e significados, e as danças são formas de preservar e expressar sua identidade cultural."),

    ("Como os indígenas se vestem atualmente?",
     "Atualmente, o modo de vestir dos indígenas varia bastante. Muitas pessoas indígenas usam roupas semelhantes às da sociedade urbana, como camisetas, calças e tênis, especialmente no dia a dia ou na cidade. Porém, em aldeias e ocasiões especiais, eles ainda usam roupas tradicionais feitas com materiais naturais, como roupas de algodão, couro, penas e pinturas corporais, que representam sua cultura e identidade. Essas vestimentas tradicionais são usadas principalmente em rituais, festas e celebrações importantes."),

    ("Quais são os principais preconceitos enfrentados pelos indígenas?",
     "Os indígenas enfrentam vários preconceitos, como o racismo, que os discrimina por sua origem e aparência; a desvalorização de suas culturas, línguas e tradições; o estereótipo de que são atrasados ou selvagens; e a dificuldade de terem seus direitos reconhecidos, como acesso à terra, educação, saúde e direitos básicos. Além disso, muitas vezes são marginalizados socialmente, sofrendo exclusão econômica e política. Esses preconceitos prejudicam sua dignidade e dificultam a preservação de suas culturas."),

    ("Como os indígenas constroem suas casas?",
     "Os indígenas constroem suas casas utilizando materiais naturais disponíveis no ambiente, como madeira, palha, folhas, cipó e barro. A construção varia conforme o povo e o clima da região, mas geralmente é feita de forma comunitária, seguindo técnicas tradicionais passadas de geração em geração. As casas, como ocas ou malocas, são projetadas para atender às necessidades do grupo, proporcionando proteção, ventilação e espaço para convivência e rituais."),

    ("De onde vem o alimento nas aldeias?",
     "O alimento nas aldeias indígenas vem principalmente da agricultura, caça, pesca e coleta de frutos, raízes e plantas da floresta ou do ambiente ao redor. Eles cultivam alimentos tradicionais como milho, mandioca, feijão e abóbora, além de pescar rios e lagos e caçar animais para complementar a dieta. Essa forma de obter alimento está ligada ao respeito pela natureza e ao conhecimento dos ciclos naturais."),

    ("Ainda se caçam ou pescam como antigamente?",
     "Muitas comunidades indígenas ainda caçam e pescam usando técnicas tradicionais, preservando saberes antigos que respeitam o equilíbrio da natureza. Essas práticas continuam importantes para a alimentação, cultura e identidade, embora em algumas regiões tenham sido adaptadas devido a mudanças ambientais, leis ou convivência com a sociedade urbana."),

    ("Como é feito o artesanato indígena?",
     "O artesanato indígena é feito com materiais naturais como madeira, fibras, sementes, cerâmica, couro e pigmentos extraídos de plantas e minerais. Cada povo utiliza técnicas tradicionais passadas de geração em geração para criar objetos que podem ser utilitários, como cestos e utensílios, ou decorativos, como colares, pinturas e esculturas. O artesanato expressa a cultura, a história e a espiritualidade do grupo, sendo também uma forma de sustento econômico para muitas comunidades."),

    ("As comunidades vendem o que produzem?",
     "Muitas comunidades indígenas vendem seus produtos, como artesanato, alimentos e objetos tradicionais, para garantir uma fonte de renda. Essa comercialização ajuda a fortalecer a economia local e a valorização da cultura indígena, além de possibilitar a sustentabilidade das aldeias. No entanto, a venda é feita geralmente de forma cuidadosa, para respeitar os valores culturais e evitar a descaracterização dos produtos."),

    ("Existem rituais de cura ou espiritualidade?",
     "Muitos povos indígenas realizam rituais de cura e espiritualidade que são fundamentais para sua cultura. Esses rituais, conduzidos por líderes espirituais como xamãs ou pajés, envolvem cânticos, danças, uso de plantas medicinais e práticas simbólicas que conectam o corpo, a mente e o espírito à natureza e aos ancestrais. Eles são usados para tratar doenças, proteger a comunidade e fortalecer a ligação espiritual do povo."),

    ("Que línguas são faladas nas aldeias do Vale do Paranhana?",
     "As principais línguas indígenas faladas são o Kaingang e o Mbya-Guarani."),

    ("As crianças indígenas aprendem a língua portuguesa também?",
     "Crianças indígenas geralmente aprendem tanto a língua portuguesa quanto a língua do seu povo. O ensino do português é importante para que elas possam se comunicar com a sociedade em geral, ter acesso à educação formal e a serviços públicos. Ao mesmo tempo, muitas comunidades valorizam e promovem o aprendizado da língua indígena para preservar sua cultura e identidade. Em algumas aldeias, há escolas bilíngues que ensinam nas duas línguas."),

    ("Há escolas nas aldeias? Como é o ensino?",
     "Muitas aldeias indígenas possuem escolas próprias, onde o ensino busca respeitar a cultura, a língua e os conhecimentos tradicionais dos povos. O ensino pode ser bilíngue, ensinando tanto a língua indígena quanto o português, e inclui conteúdos sobre a história, as práticas e o modo de vida da comunidade. Além disso, há uma valorização dos saberes ancestrais, como a agricultura, as artes e os rituais. O objetivo é formar alunos que possam conviver e atuar tanto dentro da aldeia quanto na sociedade em geral."),

    ("Como a língua indígena é preservada nas novas gerações?",
     "A preservação da língua indígena nas novas gerações acontece principalmente por meio do uso cotidiano dentro das famílias e comunidades, onde crianças aprendem naturalmente ao conviver com os mais velhos. Rituais, cantos, histórias e práticas culturais também ajudam a manter a língua viva, garantindo que o conhecimento seja transmitido de forma oral e prática entre as gerações."),

    ("Existem palavras em Kaingang ou Guarani que são comuns com o português?",
     "Algumas palavras de origem Kaingang ou Guarani entraram no português, principalmente nomes de plantas, animais, alimentos e termos relacionados à cultura indígena. Por exemplo: do Guarani, temos palavras como tapioca, mandioca, jacaré, piranha, tucano e Ivoti (nome de lugar). Do Kaingang, é menos comum, mas algumas palavras indígenas influenciaram nomes regionais e termos usados em comunidades locais, embora em menor escala que o Guarani."),

    ("Como é o relacionamento entre as aldeias e os municípios da região?",
     "O relacionamento entre as aldeias indígenas e os municípios da região pode variar bastante, mas geralmente envolve desafios e esforços de convivência. Muitas vezes, as aldeias buscam o reconhecimento de seus direitos, como a demarcação de terras e acesso a serviços públicos, enquanto os municípios precisam aprender a respeitar e incluir as comunidades indígenas em suas políticas. Em alguns lugares há parcerias e cooperação, especialmente em áreas como educação, saúde e cultura, mas também existem conflitos por causa de disputas territoriais, desentendimentos culturais e falta de compreensão mútua. O diálogo e o respeito são fundamentais para melhorar essa relação."),

    ("Existem iniciativas de preservação da cultura indígena no Vale do Paranhana?",
     "No Vale do Paranhana existem iniciativas para preservar a cultura indígena, principalmente dos povos Kaingang e Guarani. Essas ações envolvem valorização do artesanato, fortalecimento da língua e tradições, além de projetos educacionais e culturais que ajudam a manter a identidade e os saberes tradicionais vivos."),

    ("Existem lideranças femininas nas aldeias?",
     "Existem lideranças femininas nas aldeias indígenas. Embora as formas de liderança variem entre os povos, muitas mulheres ocupam papéis importantes como líderes comunitárias, educadoras, guardiãs dos saberes tradicionais e organizadoras de rituais. Embora isso não seja algo amplamente aceito em todas as aldeias, atualmente, muitas aldeias vêm valorizando cada vez mais a participação das mulheres em cargos de liderança e na defesa dos direitos indígenas."),
    
     ("O que diferencia os povos indígenas entre si?", 
     "O que diferencia os povos indígenas entre si são principalmente sua língua, cultura, organização social, territórios e tradições específicas. Cada povo tem suas próprias histórias, crenças, formas de viver, rituais, artes, modos de se relacionar com a natureza e com os outros grupos. Essas diferenças refletem a diversidade e riqueza das culturas indígenas, que se adaptaram a ambientes variados ao longo do tempo."),

    ("Quem são os Kaingang?", 
     "Os Kaingang são um povo indígena do sul do Brasil, principalmente nos estados do Rio Grande do Sul, Santa Catarina e Paraná. Eles têm uma cultura rica, com língua própria, também chamada Kaingang, que pertence à família linguística Jê. Tradicionalmente, vivem em aldeias organizadas com forte ligação à terra, praticando agricultura, caça e artesanato. Os Kaingang valorizam muito sua identidade cultural, seus rituais, músicas e tradições, e lutam pela preservação de seus territórios e direitos."),

    ("O que significa a palavra indígena?", 
     "Indígena é uma palavra de origem latina que significa natural do lugar, e é o termo correto para se referir aos habitantes originais de um território antes da chegada dos colonizadores. A palavra destaca a diversidade de povos e culturas, em contraste com o termo índio, que é considerado pejorativo por ter sido uma alcunha dada pelos colonizadores."),

    ("Quem são os Xokleng?", 
     "Os Xokleng são um povo indígena do sul do Brasil, principalmente no estado de Santa Catarina. Eles fazem parte da família linguística Jê, assim como os Kaingang, e têm uma cultura própria, com tradições, língua, rituais e organização social específicas. Historicamente, os Xokleng viviam em grandes áreas da Mata Atlântica, mas atualmente suas terras são menores e concentradas em áreas demarcadas. Eles mantêm práticas tradicionais, como a caça, a pesca, o artesanato e rituais culturais, lutando pela preservação de seus direitos e territórios."),

    ("Quais são as características dos indígenas?", 
     "Os indígenas são povos originários que possuem culturas, línguas, tradições e modos de vida próprios, desenvolvidos ao longo de milhares de anos antes da colonização. Eles têm uma forte ligação com a terra, que consideram essencial para sua identidade, espiritualidade e sobrevivência. São organizados em comunidades ou aldeias, onde mantêm práticas tradicionais como agricultura, caça, pesca, artesanato e rituais culturais. A diversidade entre os povos indígenas é grande, refletindo diferentes formas de viver, crenças e relações sociais. Além disso, valorizam a transmissão oral de conhecimentos e a preservação de sua cultura diante dos desafios da modernidade."),

    ("Qual a importância da natureza e dos espíritos para os povos indígenas?", 
     "Para os povos indígenas, a natureza e os espíritos estão profundamente interligados. A terra, os rios, animais e plantas são vistos como seres sagrados, com espíritos que devem ser respeitados. Eles acreditam que a harmonia com a natureza é essencial para a sobrevivência, realizando rituais para agradecer e pedir permissão aos espíritos antes de caçar ou colher. Os líderes espirituais, como os pajés, mediam a comunicação com esses espíritos, garantindo o equilíbrio entre os seres humanos, a natureza e o mundo espiritual."),

    ("Como a espiritualidade está presente no cotidiano da aldeia?", 
     "A espiritualidade está presente em tudo o que os povos indígenas fazem no dia a dia. Eles acreditam que a natureza tem espírito, as árvores, os rios, os animais e o sol são sagrados e devem ser respeitados. Antes de caçar, plantar ou pescar, muitas vezes fazem rezas, cantos ou rituais para pedir permissão e agradecer. Os pajés (ou curandeiros) cuidam da saúde e da ligação com os espíritos. Os mais velhos ensinam histórias e costumes que mostram como viver em equilíbrio com a natureza."),

    ("Como são fabricados os instrumentos musicais indígenas?", 
     "Os instrumentos musicais indígenas são feitos com materiais da natureza, como madeira, bambu, sementes, barro e couro. São produzidos à mão e usados em rituais, festas e danças. Cada instrumento tem significado espiritual, representando a ligação com a natureza e os espíritos. O conhecimento da fabricação é passado pelos mais velhos para manter a tradição viva."),

    ("Como os indígenas veem o contato com outras culturas?", 
     "Os indígenas veem o contato com outras culturas de formas diferentes, dependendo da experiência de cada povo. Alguns o encaram como uma oportunidade de troca e aprendizado, desde que haja respeito pelas suas tradições e modo de vida. Outros veem com cuidado ou desconfiança, pois o contato muitas vezes trouxe perda de terras, doenças e desrespeito à cultura. Em geral, eles defendem o direito de escolher como e quando se relacionar com outras culturas, mantendo viva sua identidade e autonomia."),

    ("Já houve conflitos por território no Vale do Paranhana?", 
     "Não encontrei confirmação confiável de que tenha havido conflitos documentados de disputa territorial de povos indígenas exatamente na região do Vale do Paranhana (RS)."),

    ("Como os povos indígenas se sentem em relação à preservação de suas terras?", 
     "Os povos indígenas se sentem muito ligados e responsáveis pela preservação de suas terras. Para eles, a terra não é apenas um espaço para morar, mas parte da própria vida e espiritualidade. Ela fornece alimento, abrigo, remédios e mantém a ligação com os ancestrais. Por isso, eles se preocupam e lutam para proteger suas terras contra o desmatamento, a mineração e as invasões. Preservar o território significa garantir o futuro do povo, da cultura e da natureza."),

    ("Como os indígenas cuidam dos rios, florestas e animais da região?", 
     "Os indígenas cuidam dos rios, florestas e animais com respeito e equilíbrio, porque acreditam que a natureza tem espírito e faz parte da vida. Eles usam apenas o que precisam para comer, construir e viver, sem desperdiçar. Quando caçam, pescam ou colhem frutas, agradecem e pedem permissão aos espíritos da natureza. As florestas e os rios são vistos como sagrados, por isso são mantidos limpos e preservados. Os animais são tratados com cuidado, não caçam mais do que o necessário e aproveitam tudo do que usam. Além disso, os mais velhos ensinam as crianças a respeitar a terra, as águas e os seres vivos, para que as próximas gerações continuem cuidando do ambiente. Assim, vivem em harmonia com a natureza, garantindo que ela continue dando vida para todos."),

    ("Como os povos indígenas transmitem seus conhecimentos sem livros?", 
     "Os povos indígenas transmitem seus conhecimentos por meio da fala, das histórias contadas pelos mais velhos, das tradições, danças, cantos e da convivência no dia a dia com a comunidade."),

    ("O que os indígenas esperam das próximas gerações?", 
     "Os indígenas esperam que as próximas gerações continuem respeitando a natureza, valorizando sua cultura, sua língua e suas tradições, para que seu povo e seus costumes não desapareçam."),

    ("Como os povos indígenas lidam com o avanço das cidades próximas às aldeias?", 
     "Os povos indígenas tentam proteger suas terras e costumes, dialogando com as autoridades e buscando manter suas tradições, mesmo com as mudanças trazidas pelas cidades próximas."),

    ("O que os indígenas gostariam que as pessoas não indígenas entendessem melhor sobre eles?", 
     "Os indígenas gostariam que as pessoas não indígenas entendessem que eles têm suas próprias culturas, línguas e modos de viver, que merecem respeito e que são parte importante da história e da diversidade do Brasil."),

    ("Existem alimentos ou ervas considerados sagrados?", 
     "Muitos povos indígenas consideram alguns alimentos e ervas sagrados, como o milho, a mandioca, o tabaco e certas plantas usadas em rituais de cura e espiritualidade."),

    ("Como os indígenas se relacionam com os ciclos da lua e das estações?", 
     "Os indígenas observam os ciclos da lua e das estações para plantar, pescar, caçar e realizar rituais, pois acreditam que a natureza e seus ciclos influenciam a vida e o equilíbrio do mundo."),

    ("Existem parcerias com universidades ou ONGs na preservação cultural dos indígenas?", 
     "Existem parcerias com universidades e ONGs que ajudam na preservação cultural dos povos indígenas, apoiando projetos de educação, registro das línguas, valorização das tradições e proteção das terras."),

    ("Como os Kaingang se organizam politicamente dentro da aldeia?", 
     "Os Kaingang se organizam politicamente por meio de um cacique, que é o líder da aldeia e representa o povo nas decisões importantes. Ele conta com a ajuda de conselheiros e de lideranças mais velhas, que orientam e participam das decisões coletivas. Tudo é discutido em grupo, e as decisões são tomadas pensando no bem de toda a comunidade."),

    ("Como são feitas as cerimônias de nascimento nas aldeias Kaingang?", 
     "Nas aldeias Kaingang, as cerimônias de nascimento são momentos de celebração e respeito. Quando uma criança nasce, a família e a comunidade se reúnem para dar boas-vindas e proteger o bebê espiritualmente. Os mais velhos fazem rezas e rituais com ervas e fumaça para pedir proteção e saúde. O nome da criança geralmente é escolhido com base em tradições e significados ligados à natureza ou aos ancestrais."),

    ("Quais são os principais alimentos cultivados pelos Kaingang?", 
     "Os principais alimentos cultivados pelos Kaingang incluem gêneros agrícolas básicos como milho, feijão, mandioca e moranga/abóbora. Esses alimentos, juntamente com a coleta do pinhão, compõem a base da sua alimentação tradicional."),

    ("Quais animais são mais importantes para a cultura Kaingang?", 
     "Para o povo Kaingang, os animais mais importantes são aqueles que têm valor espiritual e simbólico em seus mitos e tradições. Entre eles destacam-se: Jaguar (onça) - símbolo de força e poder. Tatu - associado à proteção e à sabedoria. Pássaros - vistos como mensageiros entre o mundo espiritual e o humano. Macaco e veado - aparecem em histórias que ensinam valores e comportamentos. Esses animais fazem parte da cosmologia Kaingang e representam a ligação entre a natureza e a vida do povo."),

    ("O que é mais valorizado dentro de uma aldeia: a coletividade ou o individualismo?", 
     "Dentro de uma aldeia indígena, a coletividade é muito mais valorizada do que o individualismo. As decisões, o trabalho, a educação das crianças e até a partilha dos alimentos são feitos pensando no bem de todos. A comunidade é vista como um conjunto interligado, em que cada pessoa tem um papel importante para o equilíbrio e a sobrevivência do grupo."),

    ("Como as comunidades Kaingang se adaptam às tecnologias modernas?", 
     "As comunidades Kaingang se adaptam às tecnologias modernas de forma equilibrada, buscando usar o que é útil sem perder suas tradições. Eles utilizam celulares, internet e redes sociais para fortalecer a comunicação entre aldeias, divulgar sua cultura e lutar por seus direitos. Além disso, computadores e ferramentas digitais são usados em escolas indígenas e projetos culturais. Mesmo com essas inovações, os Kaingang mantêm viva sua língua, rituais e modos de vida tradicionais, mostrando que é possível integrar o novo sem abandonar o que é ancestral."),

    ("O que significa o nome Kaingang?", 
     "O nome Kaingang está fortemente associado à natureza e à identidade coletiva desse povo. Em diversas fontes culturais e antropológicas, é interpretado como significando povo da floresta, gente do mato ou morador do mato, expressando a profunda relação dos Kaingang com o ambiente natural e seu modo de vida comunitário. De acordo com publicações culturais e estudos sobre o povo Kaingang, o termo pode ser formado pela junção de kaa (mato) e ingang (morador), reforçando o sentido de pertencimento à terra e à floresta. No entanto, órgãos oficiais como a FUNAI e o IBGE não apresentam uma definição linguística padronizada para o nome, o que indica que essas traduções têm caráter interpretativo e simbólico, mais do que etimológico. Assim, o significado do termo Kaingang é amplamente reconhecido na literatura como uma expressão da ligação espiritual e cultural desse povo com a natureza, embora não exista consenso formal sobre sua tradução literal."),

    ("O que acontece quando um indígena morre?", 
     "Quando um indígena do Vale do Paranhana morre, o momento é marcado por grande respeito e por rituais que expressam a ligação espiritual com a natureza e os ancestrais. As práticas variam entre os povos da região, como os Kaingang e os Guarani, mas compartilham a ideia de que a morte não representa um fim, e sim a continuação do ciclo da vida. Em geral, o corpo do falecido é preparado com pinturas e adornos feitos de elementos naturais, como urucum e jenipapo, sendo sepultado em um local considerado sagrado ou significativo para a comunidade. Durante o ritual, são entoados cantos, rezas e danças tradicionais, com o objetivo de guiar o espírito em seu caminho espiritual e manter o equilíbrio entre o mundo dos vivos e o dos mortos. Também é comum a partilha de alimentos e momentos de silêncio, em sinal de união e respeito. Esses costumes refletem a crença de que o espírito do falecido permanece presente, protegendo a aldeia e fortalecendo a relação do povo com a terra e com seus antepassados."),

    ("Como os indígenas lidam com a educação fora da aldeia?", 
     "Os indígenas que estudam fora da aldeia enfrentam desafios, mas também enxergam a educação como uma oportunidade de fortalecimento cultural e social. Muitos jovens saem de suas comunidades para estudar em escolas e universidades nas cidades, buscando novos conhecimentos que possam ser aplicados em benefício do próprio povo. No entanto, essa convivência com a sociedade não indígena pode gerar dificuldades, como o preconceito, a adaptação a novos costumes e o afastamento temporário de suas tradições. Mesmo assim, a educação é vista como um instrumento de resistência e valorização cultural, pois permite que os indígenas defendam seus direitos, compartilhem sua visão de mundo e promovam o diálogo entre culturas diferentes. Muitos estudantes mantêm o vínculo com suas aldeias, retornando com o objetivo de contribuir para o desenvolvimento comunitário e para a preservação de sua identidade."),

    ("Como é o papel das mulheres nas comunidades Kaingang?", 
     "Nas comunidades Kaingang, as mulheres têm um papel fundamental tanto na vida social quanto na preservação cultural. Elas são responsáveis por transmitir conhecimentos tradicionais, como o uso de plantas medicinais, o preparo de alimentos típicos, o artesanato e as histórias do povo, garantindo que esses saberes passem de geração em geração. Além disso, exercem funções importantes na organização da aldeia, na educação das crianças e na manutenção da harmonia familiar e espiritual. Nos últimos anos, muitas mulheres Kaingang também têm se destacado em espaços de liderança política, educação e defesa dos direitos indígenas, mostrando que o papel feminino vai além das tarefas cotidianas e está profundamente ligado à força, à sabedoria e à continuidade cultural de seu povo. Um exemplo é Joziléia Kaingang, professora e geógrafa que atua na valorização das mulheres indígenas e na promoção de políticas públicas voltadas à igualdade e ao reconhecimento dos povos originários, representando a presença ativa e transformadora das mulheres Kaingang em diferentes espaços sociais."),
     
     ("Os povos indígenas têm esportes ou brincadeiras típicas?",
     "Os povos indígenas do Rio Grande do Sul, como os Kaingang e Guarani, possuem esportes e brincadeiras tradicionais que fazem parte de sua cultura e convivência comunitária. Entre as práticas mais conhecidas estão a corrida de tora, o arco e flecha e o arremesso de lança, atividades que exigem força, resistência e cooperação. Essas modalidades são frequentemente apresentadas em eventos como os Jogos Tradicionais dos Povos Originários do Sul, realizados em aldeias do estado, onde representantes de diferentes comunidades se reúnem para celebrar o esporte, a cultura e a espiritualidade indígena. Além de competições, esses jogos têm o objetivo de preservar tradições e fortalecer os laços entre as aldeias."),
     
   ("Os indígenas têm culinária própria?",
"Os povos indígenas do Rio Grande do Sul, como os Kaingang e Guarani, possuem uma culinária própria, baseada em alimentos naturais e produzidos de forma sustentável. Entre os principais ingredientes estão o milho, a mandioca, o pinhão, o mel, o peixe e a caça, que são preparados de diferentes maneiras conforme a tradição de cada comunidade. Os Kaingang, por exemplo, valorizam o pinhão, semente da araucária típica da região, utilizado em diversas receitas e considerado símbolo de vida e fartura. Já os Guarani costumam preparar pratos à base de milho e mandioca, como o mbeyú e o chipa, alimentos tradicionais que fazem parte tanto do cotidiano quanto de celebrações religiosas e comunitárias. Esses costumes culinários expressam a relação profunda dos povos indígenas com a natureza, o respeito pelos ciclos da terra e a transmissão dos saberes alimentares entre as gerações."),

("Como os indígenas tratam os mais velhos?",
"Os povos indígenas tratam os mais velhos com profundo respeito e admiração, reconhecendo neles os guardiões da sabedoria e da memória coletiva. Entre comunidades como os Kaingang e os Guarani, no Rio Grande do Sul, os anciãos têm papel central na educação das crianças, na transmissão da língua, dos costumes e das histórias tradicionais, além de serem consultados em decisões importantes da aldeia. Os mais velhos são vistos como elos entre o passado e o presente, pois carregam o conhecimento ancestral que orienta a vida comunitária e o equilíbrio com a natureza. O cuidado, a escuta e a valorização dos anciãos fazem parte da convivência diária, reforçando o sentido de coletividade e continuidade cultural."),

("Como são os nomes indígenas e seus significados?",
"Os nomes indígenas possuem profundos significados culturais e espirituais, variando conforme o povo e a língua de origem. O nome de uma pessoa geralmente está ligado à natureza, aos animais, às plantas ou a acontecimentos importantes do nascimento. Entre os Kaingang, o nome pode refletir características da pessoa, como coragem, força ou ligação com determinados elementos naturais. Já entre os Guarani, os nomes costumam expressar virtudes, sentimentos ou relações espirituais, sendo escolhidos por líderes religiosos ou pelos mais velhos da comunidade."),

("Como os indígenas cuidam da saúde?",
"Os povos indígenas cuidam da saúde a partir de uma visão ampla e coletiva, que envolve o equilíbrio entre corpo, espírito, comunidade e natureza. Para eles, estar saudável não significa apenas não ter doenças, mas viver em harmonia com o ambiente e com os outros. Muitas comunidades utilizam práticas tradicionais, como o uso de ervas medicinais, rezas, banhos de ervas e rituais conduzidos por pajés e curandeiros, que são figuras de grande respeito e sabedoria. Essas práticas fazem parte de uma medicina tradicional transmitida de geração em geração. Ao mesmo tempo, os povos indígenas também contam com o apoio da Secretaria Especial de Saúde Indígena (SESAI), que leva atendimento médico e campanhas de vacinação às aldeias, buscando unir os saberes tradicionais e a medicina moderna."),

("Como os indígenas usam o fogo em seus rituais?",
"O fogo tem um papel sagrado para muitos povos indígenas, simbolizando vida, purificação e ligação com os ancestrais. Ele é usado em rituais, rezas e celebrações, geralmente colocado no centro das cerimônias para unir a comunidade e fortalecer a espiritualidade. Além disso, serve para purificar o ambiente e preparar alimentos coletivos, sendo um elemento essencial tanto no aspecto simbólico quanto prático."),

("Os indígenas fazem cerimônias para agradecer à natureza?",
"Muitos povos indígenas realizam cerimônias de agradecimento à natureza, reconhecendo-a como fonte de vida e espiritualidade. Esses rituais costumam envolver cantos, danças, oferendas e orações, expressando respeito pelos rios, florestas, animais e pelo solo. As cerimônias acontecem em momentos especiais, como colheitas, mudanças de estação ou após caçadas e pescas, simbolizando a gratidão e o equilíbrio entre os seres humanos e o ambiente."),

("Qual é o papel do pajé dentro da aldeia?",
"O pajé tem um papel central nas aldeias indígenas, sendo líder espiritual, curador e guardião dos saberes tradicionais. Ele é responsável por realizar rituais, curas e orientações espirituais, além de manter o equilíbrio entre o mundo humano e o espiritual. O pajé também transmite conhecimentos sobre ervas medicinais, cantos sagrados e tradições ancestrais, ensinando os mais jovens e fortalecendo a cultura do povo. Sua autoridade vem do respeito conquistado pela sabedoria e pela ligação profunda com a natureza e os espíritos."),

("Como os indígenas veem a morte e o mundo espiritual?",
"Para muitos povos indígenas, a morte não é vista como um fim, mas como uma passagem para o mundo espiritual, onde o espírito continua existindo e mantendo laços com os vivos. A vida e a morte fazem parte de um ciclo natural, em que o corpo retorna à terra e o espírito segue seu caminho junto aos ancestrais."),

("Os povos indígenas têm mitos de criação do mundo?",
"Os povos indígenas possuem narrativas de criação que explicam a origem do mundo, dos seres humanos e da natureza. Essas histórias, transmitidas oralmente entre gerações, expressam uma visão espiritual e simbólica do universo, em que tudo está conectado — a terra, os animais, as plantas e os espíritos. Embora a palavra mito seja usada academicamente, para os povos indígenas essas narrativas não são lendas ou invenções, mas verdades sagradas que orientam a vida e os valores da comunidade. Entre os Guarani, por exemplo, fala-se de Nhanderu, o Grande Pai, criador de todas as coisas. Já os Kaingang contam a origem das metades Kamé e Kairu, que representam o equilíbrio entre forças opostas da natureza. Essas histórias têm papel essencial na educação, espiritualidade e preservação cultural, mostrando como os povos indígenas compreendem e respeitam o mundo em que vivem."),

("Como os indígenas lidam com o lixo e o meio ambiente?",
"Os povos indígenas lidam com o lixo e o meio ambiente de forma respeitosa e sustentável, pois veem a natureza como parte viva de sua existência. Tradicionalmente, os resíduos gerados nas aldeias são naturais e biodegradáveis, retornando ao solo sem causar impacto. Com a chegada de produtos industrializados, surgiram desafios como o descarte de plásticos e pilhas. Para enfrentá-los, muitas comunidades, com apoio da FUNAI e da FUNASA, realizam ações de coleta seletiva, reciclagem e educação ambiental, unindo saberes tradicionais e práticas modernas."),

("O que é mais importante na cultura indígena: o saber ou o ter?",
"Na cultura indígena, o saber é muito mais importante que o ter. O conhecimento — sobre a natureza, os costumes, a espiritualidade e a convivência coletiva — é o que garante a continuidade da vida e da cultura. Esse saber é transmitido oralmente pelos mais velhos, valorizando a memória, a experiência e o respeito. O ter, no sentido material, tem pouco valor nas aldeias, pois os bens são compartilhados e usados de forma coletiva. O que realmente importa é o equilíbrio com a natureza, a solidariedade e o aprendizado constante, que fortalecem a comunidade e mantêm viva a identidade de cada povo."),

("Os povos indígenas fazem música?",
"Os povos indígenas fazem música, e ela está presente em rituais, celebrações e na vida cotidiana. Os cantos e instrumentos, como tambores, maracás e flautas, feitos com elementos da natureza, têm função espiritual, educativa e social, transmitindo histórias, valores e ensinamentos. A música indígena não é apenas lazer: é uma forma de preservar a cultura, fortalecer a comunidade e manter viva a conexão com os ancestrais e a natureza."),

("Como os indígenas aprendem a caçar e pescar?",
"Os indígenas aprendem a caçar e pescar desde pequenos, observando os mais velhos e participando das atividades junto com eles. Esse aprendizado é passado de geração em geração, por meio da prática e da convivência, respeitando sempre o equilíbrio da natureza e as épocas certas para cada tipo de caça ou pesca."),

("Como os indígenas veem o dinheiro e o comércio moderno?",
"Para muitos povos indígenas, o dinheiro não é o centro da vida. Eles valorizam mais a troca, a partilha e a colaboração dentro da comunidade. No entanto, alguns grupos utilizam o comércio moderno para vender artesanatos ou produtos naturais, buscando conciliar a tradição com as necessidades atuais."),

("Como o artesanato ajuda na preservação cultural?",
"O artesanato é uma forma de manter viva a cultura, pois carrega símbolos, histórias e saberes dos antepassados. Cada peça feita à mão representa parte da identidade do povo e ajuda a transmitir os conhecimentos tradicionais para as novas gerações."),

("Qual o papel da música nos rituais espirituais?",
"A música tem um papel sagrado nos rituais indígenas. Ela serve para se conectar aos espíritos da natureza, pedir proteção, agradecer e celebrar a vida. Os cantos e instrumentos variam entre os povos, mas todos expressam a espiritualidade e a união da comunidade."),

("O que representa o sol e a lua nas crenças indígenas?",
"O sol e a lua são vistos como forças poderosas da natureza. Em muitas tradições, o sol representa a vida, a energia e o crescimento, enquanto a lua simboliza o equilíbrio, o tempo e o ciclo da natureza. Ambos têm papéis importantes nos mitos e nas histórias dos povos."),

("Quais são os principais desafios para a juventude indígena hoje?",
"Os jovens indígenas enfrentam o desafio de equilibrar a vida tradicional com o mundo moderno. Muitos buscam estudar e trabalhar nas cidades, mas também têm o desejo de preservar sua língua, cultura e território. A discriminação e a falta de oportunidades são problemas que ainda persistem."),

("Como as novas gerações indígenas mantêm vivas as tradições dos antepassados?",
"Eles aprendem com os mais velhos, participam de rituais, danças, festas e momentos de ensino na aldeia. Além disso, muitos jovens estão usando a internet e as redes sociais para divulgar sua cultura e lutar pelos direitos de seus povos."),

("Como os povos indígenas participam de eventos culturais fora das aldeias?",
"Eles participam levando apresentações de danças, músicas, exposições de artesanato e rodas de conversa sobre sua cultura. Esses eventos são importantes para fortalecer o orgulho indígena e mostrar à sociedade a riqueza e a diversidade de suas tradições."),

("Como as comunidades indígenas lidam com a presença de não indígenas em seus territórios?",
"Cada povo tem suas próprias regras. Em geral, eles recebem visitantes com respeito, mas esperam que os não indígenas entendam e respeitem seus costumes, crenças e o modo de vida da comunidade. A entrada em áreas sagradas ou restritas costuma ser controlada."),

("O que os povos indígenas pensam sobre o futuro de suas culturas?",
"Muitos indígenas acreditam que o futuro depende da união e da resistência. Mesmo com as mudanças do mundo moderno, há um esforço constante para manter vivas as tradições, as línguas e os modos de vida que os identificam como povos originários."),

("Como os indígenas participam na defesa do meio ambiente e da floresta?",
"Eles são grandes protetores da natureza. Vivem em harmonia com o meio ambiente e defendem as florestas contra o desmatamento e a poluição. Muitos líderes indígenas participam de movimentos e conferências para denunciar abusos e propor formas sustentáveis de viver."),

("Quais são os símbolos mais usados nas pinturas corporais Kaingang e Guarani?",
"Entre os Kaingang, as pinturas costumam ter formas geométricas que representam elementos da natureza e da vida espiritual. Já os Guarani usam traços que simbolizam proteção, união e pertencimento. Cada desenho tem um significado e é usado em momentos especiais."),

("O que o governo faz para apoiar as aldeias indígenas do Vale do Paranhana?",
"O governo oferece apoio por meio de políticas públicas voltadas à saúde, educação e demarcação de terras. Também há projetos culturais e parcerias com universidades para valorizar o conhecimento indígena, embora ainda existam muitas dificuldades e falta de recursos."),

("O que representa o canto nas cerimônias espirituais indígenas?",
"O canto é uma forma de comunicação com o sagrado. Ele expressa gratidão, pedidos e sentimentos da comunidade. Em muitas cerimônias, o canto é considerado uma oração que fortalece o espírito e une todos os participantes."),

("Que línguas são faladas nas aldeias do Vale do Paranhana?",
"Nas aldeias da região, fala-se principalmente o Kaingang e o Guarani, além do português. O uso das línguas tradicionais é incentivado nas escolas e nas famílias, como forma de manter viva a identidade e a cultura dos povos indígenas locais."),

("Como a religião cristã influenciou e modificou a vida nas aldeias indígenas?",
"A chegada da religião cristã teve grande impacto sobre a vida nas aldeias indígenas, alterando costumes, crenças e modos de viver. Desde o período colonial, missionários católicos e, mais tarde, evangélicos buscaram converter os povos indígenas, muitas vezes impondo sua fé e desvalorizando as práticas espirituais tradicionais. Em diversas comunidades, isso resultou na perda de rituais, línguas e costumes ancestrais, pois muitos indígenas foram levados a abandonar suas tradições para adotar valores cristãos. No entanto, em vez de rejeitarem completamente suas crenças antigas, muitos povos recriaram suas práticas, unindo elementos do cristianismo e da espiritualidade indígena — um processo conhecido como sincretismo religioso. Hoje, há aldeias que seguem o cristianismo, outras que mantêm seus rituais tradicionais, e várias que combinam os dois, demonstrando resistência cultural e capacidade de adaptação diante das mudanças históricas."),

("Quais são as diferenças entre as habitações Kaingang, Guarani e Xokleng?",
"Os Kaingang moram em casas de taquara e palha, simples e retangulares. Os Guarani têm casas de madeira e palha e o opy, usado para rezas e rituais. Os Xokleng faziam casas de troncos e folhas perto de rios; hoje, usam também madeira ou alvenaria."),

("Como os indígenas escolhem os locais para formar uma nova aldeia?",
"A escolha do local é feita com muito cuidado e respeito à natureza. Eles observam fatores como a proximidade de rios, a fertilidade do solo, a presença de animais e plantas, e também consideram aspectos espirituais, como lugares considerados sagrados. Além disso, a decisão é tomada coletivamente, envolvendo os líderes e os anciãos, que avaliam se o local oferece boas condições para viver sem causar danos ao ambiente."),

("De que forma os indígenas participam da arte e da cultura popular brasileira?",
"Os povos indígenas influenciam a arte e a cultura do Brasil em muitos aspectos. Seus cantos, danças, grafismos, histórias e artesanatos inspiram artistas, músicos e escritores. Em várias regiões do país, os indígenas participam de festivais culturais, exposições e feiras de arte, mostrando suas tradições e valorizando o conhecimento ancestral. Além disso, elementos da cultura indígena estão presentes na música popular, na culinária, na pintura e até nas palavras da língua portuguesa que têm origem indígena, como abacaxi, tatu e pipoca."),

("Como as novas tecnologias podem ajudar na preservação das línguas indígenas?",
"As novas tecnologias podem ser grandes aliadas na preservação das línguas indígenas, ajudando a registrar, ensinar e divulgar essas línguas para as novas gerações. Recursos como gravações, aplicativos e plataformas digitais têm sido usados para manter viva a riqueza linguística e cultural dos povos originários. Projetos desenvolvidos por instituições como a FUNAI, o Instituto Socioambiental (ISA) e a UNESCO produzem materiais bilíngues, jogos e ferramentas digitais que fortalecem o uso das línguas indígenas nas escolas e nas comunidades. Tecnologias como eu :) — um chatbot criado para responder dúvidas sobre os povos indígenas do Vale do Paranhana — também mostram como a inovação pode aproximar as pessoas desse conhecimento e contribuir para sua valorização. Assim, a tecnologia, quando usada com sensibilidade e respeito, torna-se uma ponte entre tradição e futuro, ajudando a preservar identidades e a manter vivas as vozes dos povos indígenas.")

]

def preprocess(text):
    return text.lower().replace("?", "").replace(".", "").replace("‘", "").replace("’", "").replace("'", "").replace("´", "").replace("^", "").replace("~", "").replace(",", "").split()

vocabulary = list(set(word for question, _ in dataset for word in preprocess(question)))

def preprocess_c(palavras):
    resultado = []  
    for palavra in palavras:  
        melhor = palavra 
        menor = 1
        for word in vocabulary:  
            distancia = character_distance(palavra, word) 
            if distancia < menor and distancia < 0.04: 
                menor = distancia  
                melhor = word 
        resultado.append(melhor) 
     
    return resultado  


def vectorize(text):
    words = preprocess(text)
    words = preprocess_c(words)
    return [words.count(word) for word in vocabulary]

def similarity(vec1, vec2):
    
    dot = sum(a*b for a, b in zip(vec1, vec2))
    
    norm1 = math.sqrt(sum(a*a for a in vec1))
    norm2 = math.sqrt(sum(b*b for b in vec2))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0
    
def answer(question):
    vec = vectorize(question)
    best_score = 0
    best_answer = "Desculpe, não sei responder isso ainda."
    for q, a in dataset:
        score = similarity(vec, vectorize(q))
        if score > best_score:
            best_score = score
            best_answer = a
    return best_answer

print("Chatbot indígena do Vale do Paranhana iniciado! (digite 'sair' para encerrar)\n")
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Bot: Até mais! ")
        break
    print("Bot:", answer(user_input))
