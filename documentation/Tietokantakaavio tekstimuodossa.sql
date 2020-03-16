CREATE TABLE `Kayttajat` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `kayttaja` text,
  `salasana` text
);

CREATE TABLE `Aiheet` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `aihe` text
);

CREATE TABLE `Lukijat` (
  `viesti_id` FK,
  `kayttaja_id` FK
);

CREATE TABLE `Viestit` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `sisalto` text,
  `aihe_id` FK,
  `kayttaja_id` FK,
  `paivamaara` text,
  `aika` text,
  `vastaus` text
);

ALTER TABLE `Lukijat` ADD FOREIGN KEY (`viesti_id`) REFERENCES `Viestit` (`id`);

ALTER TABLE `Lukijat` ADD FOREIGN KEY (`kayttaja_id`) REFERENCES `Kayttajat` (`id`);

ALTER TABLE `Viestit` ADD FOREIGN KEY (`aihe_id`) REFERENCES `Aiheet` (`id`);

ALTER TABLE `Viestit` ADD FOREIGN KEY (`kayttaja_id`) REFERENCES `Kayttajat` (`id`);
