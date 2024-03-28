SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de données :  `license`
--

-- --------------------------------------------------------

--
-- Structure de la table `site`
--

CREATE TABLE `avis` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `site`
--

INSERT INTO `site` (`id`, `name`) VALUES
(1, 'Saint-Malo'),
(2, 'Lorient'),
(3, 'Vannes'),
(4, 'Nantes'),
(5, 'Rennes');

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

CREATE TABLE `categorie` (
  `Id_Categorie` int(11) NOT NULL,
  `NomCategorie` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `categorie`
--

INSERT INTO `categorie` (`Id_Categorie`, `NomCategorie`) VALUES
(1, 'Plate-forme'),
(2, 'Sport'),
(3, 'Point & click'),
(4, 'RPG'),
(5, 'Action/Aventure'),
(6, 'FPS'),
(7, 'Divers');

-- --------------------------------------------------------

--
-- Structure de la table `classer`
--

CREATE TABLE `classer` (
  `Id_Article` int(11) NOT NULL,
  `Id_Categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `classer`
--

INSERT INTO `classer` (`Id_Article`, `Id_Categorie`) VALUES
(1, 5),
(2, 3),
(2, 7),
(3, 5),
(4, 4),
(5, 5),
(6, 2);

-- --------------------------------------------------------

--
-- Structure de la table `image`
--

CREATE TABLE `image` (
  `Id_Image` int(11) NOT NULL,
  `Chemin` varchar(250) NOT NULL,
  `Id_Article` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `image`
--

INSERT INTO `image` (`Id_Image`, `Chemin`, `Id_Article`) VALUES
(1, 'ImagesBD/1/Zelda_1.jpg', 1),
(2, 'ImagesBD/1/Zelda_2.jpg', 1),
(3, 'ImagesBD/1/Zelda_3.jpg', 1),
(4, 'ImagesBD/1/Zelda_4.jpg', 1),
(5, 'ImagesBD/1/Zelda_5.jpg', 1),
(6, 'ImagesBD/1/Zelda_6.jpg', 1),
(7, 'ImagesBD/2/Deponia_1.jpg', 2),
(8, 'ImagesBD/2/Deponia_2.jpg', 2),
(9, 'ImagesBD/2/Deponia_3.jpg', 2),
(10, 'ImagesBD/2/Deponia_4.jpg', 2),
(11, 'ImagesBD/2/Deponia_5.jpg', 2),
(12, 'ImagesBD/2/Deponia_6.jpg', 2),
(13, 'ImagesBD/3/Okami_1.jpg', 3),
(14, 'ImagesBD/3/Okami_2.jpg', 3),
(15, 'ImagesBD/3/Okami_4.jpg', 3),
(16, 'ImagesBD/3/Okami_5.jpg', 3),
(17, 'ImagesBD/3/Okami_6.jpg', 3),
(18, 'ImagesBD/4/Witcher_1.jpg', 4),
(19, 'ImagesBD/4/Witcher_2.jpg', 4),
(20, 'ImagesBD/4/Witcher_4.jpg', 4),
(21, 'ImagesBD/4/Witcher_5.jpg', 4),
(22, 'ImagesBD/5/Pokemon_1.jpg', 5),
(23, 'ImagesBD/5/Pokemon_2.jpg', 5),
(24, 'ImagesBD/5/Pokemon_3.jpg', 5),
(25, 'ImagesBD/5/Pokemon_4.jpg', 5),
(26, 'ImagesBD/5/Pokemon_5.jpg', 5),
(27, 'ImagesBD/5/Pokemon_6.jpg', 5),
(28, 'ImagesBD/6/FIFA_1.jpg', 6),
(29, 'ImagesBD/6/FIFA_2.jpg', 6),
(30, 'ImagesBD/6/FIFA_3.jpg', 6);

-- --------------------------------------------------------

--
-- Structure de la table `membre`
--

CREATE TABLE `membre` (
  `Id_Membre` int(11) NOT NULL,
  `Login` varchar(100) NOT NULL,
  `MotDePasse` varchar(100) NOT NULL,
  `EMail` varchar(100) NOT NULL,
  `DateCreation` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DateDerniereConnexion` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Role` enum('Utilisateur','Administrateur') NOT NULL DEFAULT 'Utilisateur'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `membre`
--

INSERT INTO `membre` (`Id_Membre`, `Login`, `MotDePasse`, `EMail`, `DateCreation`, `DateDerniereConnexion`, `Role`) VALUES
(1, 'mouton', 'motdepasse', 'mouton@mouton.mouton', '2022-10-19 20:28:09', '2022-10-19 20:28:09', 'Utilisateur'),
(2, 'RT', 'motdepasse', 'RT@StMaloRT.fr', '2022-10-19 20:29:57', '2022-10-19 20:29:57', 'Administrateur'),
(3, 'doooo', 'motdepasse', 'doooo@oo.oo', '2022-10-19 20:33:36', '2022-10-19 20:33:36', 'Utilisateur'),
(4, 'Kilian', '1Mot2Passe', 'kilian.fa2g2@etudiant.univ-rennes1.fr', '2023-10-17 15:44:50', '2023-10-17 15:44:50', 'Utilisateur'),
(5, 'Kilian', '1Mot2Passe', 'kilian.fa2g2@etudiant.univ-rennes1.fr', '2023-10-17 15:47:03', '2023-10-17 15:47:03', 'Utilisateur');

-- --------------------------------------------------------

--
-- Structure de la table `rediger`
--

CREATE TABLE `rediger` (
  `Id_Article` int(11) NOT NULL,
  `Id_Membre` int(11) NOT NULL,
  `DateModificationArticle` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `rediger`
--

INSERT INTO `rediger` (`Id_Article`, `Id_Membre`, `DateModificationArticle`) VALUES
(1, 1, '2022-10-21 17:22:39'),
(2, 2, '2022-10-21 17:22:39'),
(3, 1, '2022-10-21 17:23:01'),
(4, 3, '2022-10-21 17:23:01'),
(5, 1, '2022-10-21 17:23:17'),
(6, 2, '2022-10-21 17:23:17');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `avis`
--
ALTER TABLE `avis`
  ADD PRIMARY KEY (`Id_Avis`),
  ADD KEY `fk_membre_avis` (`Id_Membre`),
  ADD KEY `fk_article_avis` (`Id_Article`);

--
-- Index pour la table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`Id_Categorie`);

--
-- Index pour la table `classer`
--
ALTER TABLE `classer`
  ADD PRIMARY KEY (`Id_Article`,`Id_Categorie`),
  ADD KEY `fk_categorie_illlustrer` (`Id_Categorie`);

--
-- Index pour la table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`Id_Image`),
  ADD KEY `fk_article` (`Id_Article`);

--
-- Index pour la table `membre`
--
ALTER TABLE `membre`
  ADD PRIMARY KEY (`Id_Membre`);

--
-- Index pour la table `rediger`
--
ALTER TABLE `rediger`
  ADD PRIMARY KEY (`Id_Article`,`Id_Membre`),
  ADD KEY `fk_membre_redaction` (`Id_Membre`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `avis`
--
ALTER TABLE `avis`
  MODIFY `Id_Avis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `categorie`
--
ALTER TABLE `categorie`
  MODIFY `Id_Categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `image`
--
ALTER TABLE `image`
  MODIFY `Id_Image` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT pour la table `membre`
--
ALTER TABLE `membre`
  MODIFY `Id_Membre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `avis`
--
ALTER TABLE `avis`
  ADD CONSTRAINT `fk_article_avis` FOREIGN KEY (`Id_Article`) REFERENCES `article` (`Id_Article`),
  ADD CONSTRAINT `fk_membre_avis` FOREIGN KEY (`Id_Membre`) REFERENCES `membre` (`Id_Membre`);

--
-- Contraintes pour la table `classer`
--
ALTER TABLE `classer`
  ADD CONSTRAINT `fk_article_illustrer` FOREIGN KEY (`Id_Article`) REFERENCES `article` (`Id_Article`),
  ADD CONSTRAINT `fk_categorie_illlustrer` FOREIGN KEY (`Id_Categorie`) REFERENCES `categorie` (`Id_Categorie`);

--
-- Contraintes pour la table `image`
--
ALTER TABLE `image`
  ADD CONSTRAINT `fk_article` FOREIGN KEY (`Id_Article`) REFERENCES `article` (`Id_Article`);

--
-- Contraintes pour la table `rediger`
--
ALTER TABLE `rediger`
  ADD CONSTRAINT `fk_article_redaction` FOREIGN KEY (`Id_Article`) REFERENCES `article` (`Id_Article`),
  ADD CONSTRAINT `fk_membre_redaction` FOREIGN KEY (`Id_Membre`) REFERENCES `membre` (`Id_Membre`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
