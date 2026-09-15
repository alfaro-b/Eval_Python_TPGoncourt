SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `publisher`
--

DROP TABLE IF EXISTS publisher;
CREATE TABLE IF NOT EXISTS publisher(
   id_publisher INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_publisher)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `publisher`
--

INSERT INTO publisher (name) VALUES
('Albin Michel'),
('P.O.L'),
('Grasset'),
('Robert Laffont'),
('Actes Sud'),
('L''Iconoclaste'),
('Gallimard'),
('Flammarion'),
('Verdier'),
('Minuit'),
('Maurice Nadeau');


-- --------------------------------------------------------

--
-- Structure de la table `selection`
--
DROP TABLE IF EXISTS selection;
CREATE TABLE IF NOT EXISTS selection(
   id_selection INT NOT NULL AUTO_INCREMENT,
   number INT NOT NULL,
   date_ DATE,
   PRIMARY KEY(id_selection)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `selection`
--

INSERT INTO `selection` (`id_selection`, `number`, `date_`) VALUES
(NULL, '1', '2026-09-02'),
(NULL, '2', '2026-10-06'),
(NULL, '3', '2026-10-27');


-- --------------------------------------------------------

--
-- Structure de la table `person`
--
DROP TABLE IF EXISTS person;
CREATE TABLE IF NOT EXISTS person(
   id_person INT NOT NULL AUTO_INCREMENT,
   last_name VARCHAR(50) NOT NULL,
   first_name VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_person)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Jaenada', 'Philippe');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Godard', 'Anne');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Haenel', 'Yannick');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Hassaine', 'Lilia');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Devillers', 'Sonia');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Chennevière', 'Louise');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Rolin', 'Olivier');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Devi', 'Ananda');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Prudhomme', 'Sylvain');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Mélois', 'Clémentine');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Bergmann', 'Boris');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Jouannais', 'Jean-Yves');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Grondeau', 'Olivier');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Marsantes', 'Emma');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Trigano', 'Patrice');
INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES (NULL, 'Orélien', 'Thélyson');

INSERT INTO person (last_name, first_name) VALUES
('Decoin', 'Didier'),
('Chandernagor', 'Françoise'),
('Ben Jelloun', 'Tahar'),
('Constant', 'Paule'),
('Claudel', 'Philippe'),
('Assouline', 'Pierre'),
('Schmitt', 'Éric-Emmanuel'),
('Laurens', 'Camille'),
('Bruckner', 'Pascal'),
('Angot', 'Christine');

-- --------------------------------------------------------

--
-- Structure de la table `author`
--
DROP TABLE IF EXISTS author;
CREATE TABLE IF NOT EXISTS author(
   id_author INT NOT NULL AUTO_INCREMENT,
   biography VARCHAR(500),
   id_person INT NOT NULL,
   PRIMARY KEY(id_author),
   FOREIGN KEY(id_person) REFERENCES Person(id_person)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`id_author`, `biography`, `id_person`) VALUES
(NULL, 'Philippe Jaenada est l\'auteur d\'une douzaine de romans, dont Le Chameau sauvage (Julliard, 1997, prix de Flore), La Petite Femelle (2015) et La Serpe (2017, prix Femina) et plus récemment, chez Mialet-Barrault Éditeurs, Au printemps des monstres et La désinvolture est une bien belle chose (2021 et 2024). Il rejoint en cette rentrée littéraire les Éditions Flammarion.', '1'),
(NULL,'Anne Godard est née à Paris en 1971, elle enseigne la littérature et l\'écriture créative à l\'université Sorbonne-Nouvelle. Elle a publié aux Éditions de Minuit L\'Inconsolable en 2006 (prix RTL-Lire) et Une chance folle en 2017 (prix Alain Spiess du deuxième roman). Nous aussi est son troisième roman.','2'),
(NULL,'Yannick Haenel a notamment publié Cercle (prix Décembre 2007 et prix Roger Nimier 2008), Jan Karski (prix Interallié et prix du Roman Fnac 2009) et Tiens ferme ta couronne (prix Médicis 2017).','3'),
(NULL,'Lilia Hassaine est notamment l\'autrice de Panorama (2023, prix Renaudot des lycéens). JE est son quatrième roman.','4'),
(NULL,'Sonia Devillers est journaliste dans la matinale de France Inter et présentatrice du « Dessous des images » sur Arte. Son premier livre, Les Exportés (Flammarion, 2022), raconte comment sa famille a fui la Roumanie communiste.','5'),
(NULL,NULL,'6'),
(NULL,NULL,'7'),
(NULL,'Née à l\'île Maurice, Ananda Devi est l\'autrice d\'une oeuvre récompensée par de nombreux prix et traduite en une douzaine de langues. Parmi ses livres les plus marquants, on peut citer Ève de ses décombres (Gallimard, 2006, prix des Cinq Continents, prix RFO, prix Télévision Suisse Romande), Le Sari vert (Gallimard 2009, prix Louis Guilloux), Le Rire des déesses (Grasset, 2021, prix Femina des lycéens) et Le Jour des caméléons (Grasset, 2023, prix de la Langue française). Elle a reçu le prestigieux prix américain Neustadt 2024 pour l\'ensemble de son oeuvre.','8'),
(NULL,'Sylvain Prudhomme est l\'auteur de romans, récits et reportages salués par la critique et traduits à l\'étranger. Il a reçu le prix Femina en 2019 pour Par les routes. L\'Enfant dans le taxi a paru en 2023 aux Éditions de Minuit. Coyote, récit d\'un voyage le long de la frontière américano-mexicaine, a reçu le prix Nicolas Bouvier 2025.','9'),
(NULL,'Clémentine Mélois est née en 1980. Elle est notamment l\'autrice, aux Editions Grasset, de Cent titres. Sinon j\'oublie, Dehors, la tempête, ainsi que du très remarqué Alors c\'est bien (« L\'Arbalète », Editions Gallimard, 2024).','10'),
(NULL,'Boris Bergmann est né à Paris en 1992. Il est l\'auteur de cinq romans dont Nage Libre (prix de la Vocation 2018) et Les Corps insurgés (Prix Fénéon 2020). Il a été pensionnaire de la Villa Medicis et de la Villa Kujoyama. Il a organisé des expositions en France et à l\'étranger (autour de l\'oeuvre de René Daumal, notamment) et collabore en tant qu\'éditeur associé à la revue d\'art et de littérature Magma. Minotaure est son premier roman autobiographique.','11'),
(NULL,'Jean-Yves Jouannais, né en 1964, est professeur à l\'École nationale supérieure des beaux-arts de Paris. Il a publié, notamment, L\'Idiotie (Beaux-Arts livres), Artistes sans oeuvres (Verticales), Les Barrages de sable (Grasset). De 2008 à 2024, il est l\'auteur du cycle de conférences-performances, L\'Encyclopédie des guerres, au Centre Pompidou (Paris).','12'),
(NULL,'Après des études littéraires et des emplois de libraire, Olivier Grondeau est parti huit ans sur les routes, avant d\'être arrêté en Iran. Libéré en mars 2025, il poursuit désormais des études d\'anthropologie. L\'écriture l\'a toujours accompagné. Joseph dans la nuit est son premier livre.','13'),
(NULL,NULL,'14'),
(NULL,NULL,'15'),
(NULL,'Né en 1988, Thélyson Orélien est un auteur québécois d\'origine haïtienne. Poète et critique, il construit une oeuvre habitée par la mémoire, l\'exil et la question de l\'appartenance. Depuis sa publication au Québec par les Éditions du Boréal, C\'était ça ou mourir rencontre un écho international exceptionnel et est en cours de traduction dans plus de vingt langues. Un premier roman phénomène qui révèle une grande voix de la littérature contemporaine.','16')
;


-- --------------------------------------------------------

--
-- Structure de la table `jury_member`
--
DROP TABLE IF EXISTS jury_member;
CREATE TABLE IF NOT EXISTS jury_member(
   id_jury_member INT NOT NULL AUTO_INCREMENT,
   is_president BOOLEAN NOT NULL DEFAULT FALSE,
   id_person INT NOT NULL,
   PRIMARY KEY(id_jury_member),
   FOREIGN KEY(id_person) REFERENCES Person(id_person)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `jury_member`
--

INSERT INTO jury_member (id_person) VALUES
(17), -- Didier Decoin
(18), -- Françoise Chandernagor
(19), -- Tahar Ben Jelloun
(20), -- Paule Constant
(22), -- Pierre Assouline
(23), -- Éric-Emmanuel Schmitt
(24), -- Camille Laurens
(25), -- Pascal Bruckner
(26); -- Christine Angot
INSERT INTO jury_member (is_president, id_person) VALUES
(TRUE, 21); -- Philippe Claudel

-- --------------------------------------------------------

--
-- Structure de la table `book`
--
DROP TABLE IF EXISTS book;
CREATE TABLE IF NOT EXISTS book(
   id_book INT NOT NULL AUTO_INCREMENT,
   title VARCHAR(50),
   summary VARCHAR(2000),
   publication_date DATE,
   nbr_pages INT,
   isbn VARCHAR(13),
   publisher_price DECIMAL(5,2),
   id_author INT NOT NULL,
   id_publisher INT NOT NULL,
   PRIMARY KEY(id_book),
   FOREIGN KEY(id_author) REFERENCES Author(id_author),
   FOREIGN KEY(id_publisher) REFERENCES Publisher(id_publisher)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO book
(
    title,
    summary,
    publication_date,
    nbr_pages,
    isbn,
    publisher_price,
    id_author,
    id_publisher
)
VALUES

(
    'L''inconnue du quai de Javel',
    'En 1949, Louise Cansot, modèle très demandé à Montparnasse, est retrouvée morte quai de Javel. Soixante-quinze ans plus tard, Philippe Jaenada reprend cette affaire non élucidée et mène sa propre enquête.',
    '2026-08-12',
    528,
    '9782080490896',
    23.00,
    1,
    (SELECT id_publisher FROM publisher WHERE name = 'Flammarion')
),

(
    'Nous aussi',
    'Les membres d''une grande famille privilégiée vivent dans un univers très soudé où le groupe prime sur les individualités. Cet équilibre se fissure lorsqu''un événement vient bouleverser les certitudes familiales.',
    '2026-08-19',
    240,
    '9782330225575',
    20.00,
    2,
    (SELECT id_publisher FROM publisher WHERE name = 'Actes Sud')
),

(
    'La solitude des professeurs est infinie',
    'Jean Deichel, jeune professeur de français, effectue son stage dans un collège de banlieue parisienne. Il découvre à la fois les difficultés du métier, sa violence et les joies profondes que peut procurer l''enseignement.',
    '2026-08-20',
    320,
    '9782073161925',
    21.50,
    3,
    (SELECT id_publisher FROM publisher WHERE name = 'Gallimard')
),

(
    'Je',
    'En Jamaïque en 1831, Antoinette Cosway rencontre Edward Rochester. Leur relation passionnelle devient progressivement destructrice. Le roman redonne une voix au personnage de la première épouse de Rochester dans Jane Eyre.',
    '2026-08-20',
    256,
    '9782073099945',
    21.00,
    4,
    (SELECT id_publisher FROM publisher WHERE name = 'Gallimard')
),

(
    'Le fabuleux piano',
    'Sonia Devillers enquête sur un piano à queue dérobé pendant l''Occupation. Cette recherche fait ressurgir l''histoire d''une famille d''éditeurs de musique persécutée pendant la Seconde Guerre mondiale.',
    '2026-08-27',
    288,
    '9782221286807',
    21.00,
    5,
    (SELECT id_publisher FROM publisher WHERE name = 'Robert Laffont')
),

(
    'Faire la peau',
    'Un récit consacré aux relations complexes entre les mères et leurs filles, à la transmission et aux sentiments contradictoires qui peuvent traverser ces liens familiaux.',
    '2026-08-20',
    288,
    '9782818063583',
    21.00,
    6,
    (SELECT id_publisher FROM publisher WHERE name = 'P.O.L')
),

(
    'La guerre éternelle',
    'À partir de la guerre de Troie et des paysages de la Troade, Olivier Rolin interroge la permanence de la guerre à travers l''Histoire et les traces qu''elle laisse dans les mémoires.',
    '2026-08-20',
    224,
    '9782073121349',
    20.00,
    7,
    (SELECT id_publisher FROM publisher WHERE name = 'Gallimard')
),

(
    'Chronique d''un royaume perdu',
    'Dans le village mauricien du Bouchon, quatre générations se succèdent depuis l''époque de l''esclavage. Le roman mêle histoire familiale, violences, amours et mémoire de l''île Maurice.',
    '2026-08-19',
    464,
    '9782246846949',
    24.00,
    8,
    (SELECT id_publisher FROM publisher WHERE name = 'Grasset')
),

(
    'De l''autre côté du lac',
    'Près d''un lac de haute montagne, un groupe de chercheurs travaille aux abords d''une réserve interdite. Après plusieurs événements inquiétants et la découverte d''un corps, une photographe décide de rester seule sur place avant de disparaître à son tour.',
    '2026-08-27',
    288,
    '9782707358233',
    22.00,
    9,
    (SELECT id_publisher FROM publisher WHERE name = 'Minuit')
),

(
    'Choses que je croyais perdues',
    'Après une séparation, une jeune femme prépare son déménagement. Les objets qu''elle emballe réveillent les souvenirs de sa relation et l''amènent à réfléchir aux traces laissées par une histoire d''amour.',
    '2026-08-20',
    176,
    '9782073162854',
    19.00,
    10,
    (SELECT id_publisher FROM publisher WHERE name = 'Gallimard')
),

(
    'Minotaure',
    'Dans un récit autobiographique, Boris Bergmann explore les relations familiales, le désir, l''amour et la difficulté de trouver sa place face aux figures qui ont marqué son existence.',
    '2026-08-19',
    256,
    '9782226511874',
    20.90,
    11,
    (SELECT id_publisher FROM publisher WHERE name = 'Albin Michel')
),

(
    'Une forêt',
    'À travers une histoire située dans le contexte de la guerre, Jean-Yves Jouannais propose un court roman autour de la mémoire, des hommes et de leur rapport au monde vivant.',
    '2026-01-02',
    112,
    '9782226499523',
    16.90,
    12,
    (SELECT id_publisher FROM publisher WHERE name = 'Albin Michel')
),

(
    'Joseph dans la nuit',
    'Lors d''un voyage vers l''Asie, Olivier Grondeau est arrêté en Iran et accusé d''espionnage. Emprisonné pendant deux ans et demi, il raconte comment la poésie, la mémoire et l''imaginaire lui permettent de résister à l''enfermement.',
    '2026-08-20',
    256,
    '9782378805975',
    19.90,
    13,
    (SELECT id_publisher FROM publisher WHERE name = 'L''Iconoclaste')
),

(
    'N''efface pas mes cercles',
    'À partir du suicide d''une femme en 1980, une narratrice remonte l''histoire de sa famille et cherche à comprendre les événements qui ont conduit au drame, sur fond de guerre, de patriarcat et de colonisation.',
    '2026-08-20',
    160,
    '9782378562953',
    19.50,
    14,
    (SELECT id_publisher FROM publisher WHERE name = 'Verdier')
),

(
    'Bataille au procès',
    'En 1956, Georges Bataille témoigne au procès de l''éditeur Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. Le procès conduit l''écrivain à revisiter sa vie, ses idées et son rapport à la littérature.',
    '2026-08-21',
    136,
    '9782862316857',
    19.00,
    15,
    (SELECT id_publisher FROM publisher WHERE name = 'Maurice Nadeau')
),

(
    'C''était ça ou mourir',
    'Après l''embrasement de son quartier à Port-au-Prince, Jonas Dorléon quitte Haïti. De la République dominicaine à l''Amérique du Sud puis vers le nord du continent, il entreprend un long voyage dans l''espoir d''atteindre le Canada.',
    '2026-08-19',
    272,
    '9782246847069',
    21.50,
    16,
    (SELECT id_publisher FROM publisher WHERE name = 'Grasset')
);


-- --------------------------------------------------------

--
-- Structure de la table `main_character`
--
DROP TABLE IF EXISTS main_character;
CREATE TABLE IF NOT EXISTS main_character(
   id_main_character INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(50),
   id_book INT NOT NULL,
   PRIMARY KEY(id_main_character),
   FOREIGN KEY(id_book) REFERENCES Book(id_book)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



--
-- Déchargement des données de la table `main_character`
--

INSERT INTO `main_character` (`id_main_character`, `name`, `id_book`) VALUES
(NULL, 'Louise Cansot', '1'), (NULL, 'inspecteur-chef Ferrière', '1'),
(NULL,'Jean Deichel', '3'),
(NULL, 'Antoinette Cosway', '4'), (NULL, 'Edward Rochester', '4'),
(NULL, 'un enfant timide', '8'),
(NULL, 'une photographe', '9'),
(NULL, 'une jeune femme', '10'),
(NULL, 'Olivier', '13'),
(NULL, 'Georges Bataille', '15'), (NULL, 'Jean-Jacques Pauvert', '15'),
(NULL, 'Jonas Dorléon', '16');
-- --------------------------------------------------------

--
-- Structure de la table `Belong`
--
DROP TABLE IF EXISTS belong;
CREATE TABLE IF NOT EXISTS belong(
   id_book INT NOT NULL,
   id_selection INT NOT NULL,
   votes_number INT,
   PRIMARY KEY(id_book, id_selection),
   FOREIGN KEY(id_book) REFERENCES Book(id_book),
   FOREIGN KEY(id_selection) REFERENCES Selection(id_selection)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Déchargement des données de la table `belong`
--

INSERT INTO belong (id_book, id_selection, votes_number) VALUES
(1, 1, NULL),
(2, 1, NULL),
(3, 1, NULL),
(4, 1, NULL),
(5, 1, NULL),
(6, 1, NULL),
(7, 1, NULL),
(8, 1, NULL),
(9, 1, NULL),
(10, 1, NULL),
(11, 1, NULL),
(12, 1, NULL),
(13, 1, NULL),
(14, 1, NULL),
(15, 1, NULL),
(16, 1, NULL);