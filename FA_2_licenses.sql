--
-- Base de données :  license
--

-- --------------------------------------------------------

--
-- Structure de la table site
--

CREATE TABLE site (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

--
-- Contenu de la table site
--

INSERT INTO site (name) VALUES
('Saint-Malo'),
('Lorient'),
('Vannes'),
('Nantes'),
('Rennes');

-- --------------------------------------------------------

--
-- Structure de la table provider
--

CREATE TABLE provider (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);


--
-- Contenu de la table provider
--

INSERT INTO provider (name) VALUES
('Microsoft'),
('Adobe'),
('Bitdefender');

-- --------------------------------------------------------

--
-- Structure de la table product
--

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    nb_licenses INT,
    nb_used_licenses INT,
    provider_id INT,
    FOREIGN KEY (provider_id)
        REFERENCES provider(id),
    site_id INT,
    FOREIGN KEY (site_id)
        REFERENCES site(id)
);

--
-- Contenu de la table product
--

INSERT INTO product (name, nb_licenses, nb_used_licenses, provider_id, site_id) VALUES
('Windows 10', 50, 45, 1, 1),
('Windows 10', 30, 23, 1, 2),
('Windows 10', 70, 62, 1, 4),
('Windows 11', 36, 24, 1, 3),
('Windows 11', 12, 11, 1, 5),
('Acrobat Reader', 60, 60, 2, 1),
('Acrobat Reader', 43, 24, 2, 2),
('Acrobat Reader', 65, 54, 2, 3),
('Acrobat Reader', 24, 22, 2, 4),
('Acrobat Reader', 14, 9, 2, 5),
('GravityZone Anti-virus', 100, 90, 3, 1),
('GravityZone Anti-virus', 75, 50, 3, 2),
('GravityZone Anti-virus', 48, 45, 3, 3);

-- --------------------------------------------------------

--
-- Structure de la table license
--

CREATE TABLE license (
    id SERIAL PRIMARY KEY,
    key VARCHAR(35) NOT NULL,
    date_start DATE,
    date_expiration DATE,
    is_used BOOLEAN,
    user_id INT,
    product_id INT,
    FOREIGN KEY (product_id)
        REFERENCES product(id)
);

--
-- Contenu de la table image
--

INSERT INTO license (key, date_start, date_expiration, is_used, user_id, product_id) VALUES
('VK7JG-NPHTM-C97JM-9MPGT-3V66T', '2024-01-01', '2026-12-31', true, 1, 1),
('TX9XD-98N7V-6WMQ6-BX7FG-H8Q99', '2024-01-01', '2026-12-31', true, 7, 2),
('BPPR9-FWDCX-D2C8J-H872K-2YT43', '2024-01-01', '2026-12-31', true, 4, 3),
('RPH2V-TTNVB-4X9Q3-TJR4H-KHJW4', '2024-01-01', '2026-12-31', false, 12, 4),
('BW6C2-QMPVW-D7KKK-3GKT6-VCFB2', '2024-01-01', '2026-12-31', false, 3, 5),
('Q269N-WFGWX-YVC9B-4J6C9-T83GX', '2024-01-01', '2026-12-31', true, 35, 6),
('82NFX-8DJQP-P6BBQ-THF9C-7CG2H', '2024-01-01', '2026-12-31', false, 22, 7),
('IYVX9-NTFWV-6MDM3-9PT4T-4M68B', '2024-01-01', '2026-12-31', true, 9, 8),
('MRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J', '2024-01-01', '2026-12-31', true, 2, 9),
('ABC12-3DEF4-56GHI-789JK-L012M', '2024-02-15', '2026-10-30', true, 5, 10),
('XYZ98-7WXY6-54VWX-321TU-V098S', '2024-03-20', '2026-09-25', false, 8, 11),
('PQR98-7STU6-54VWX-321YZ-T098A', '2024-04-25', '2026-08-20', true, 11, 12),
('JKL12-3MNO4-56PQR-789ST-U012V', '2024-05-30', '2026-07-15', false, 14, 13),
('EFG98-7HIJ6-54KLM-321NO-P098Q', '2024-06-10', '2026-06-30', true, 17, 1),
('TUV12-3WXY4-56ABC-789DE-F012G', '2024-07-15', '2026-05-25', false, 20, 2),
('MNO98-7PQR6-54STU-321VW-X098Y', '2024-08-20', '2026-04-20', true, 23, 3),
('DEF12-3GHI4-56JKL-789MNO-P012Q', '2024-09-25', '2026-03-15', false, 26, 4),
('YZT98-7ABC6-54DEF-321GHI-J098K', '2024-10-30', '2026-02-28', true, 29, 5),
('GHI12-3JKL4-56MNO-789PQR-S012T', '2024-11-05', '2026-01-10', false, 32, 6),
('VWX98-7YZT6-54ABC-321DEF-G098H', '2024-12-10', '2025-12-31', true, 35, 7),
('STU12-3VWX4-56XYZ-789ABC-D012E', '2025-01-15', '2025-11-20', false, 38, 8),
('JKL98-7MNO6-54PQR-321ST-U098V', '2025-02-20', '2025-10-15', true, 41, 9),
('PQR12-3STU4-56VWX-789XYZ-012AB', '2025-03-25', '2025-09-30', false, 44, 10),
('DEF98-7GHI6-54JKL-321MNO-098PQ', '2025-04-30', '2025-08-05', true, 47, 11),
('XYZ12-3ABC4-56DEF-789GHI-J012K', '2025-05-05', '2025-07-01', false, 50, 12),
('MNO98-7PQR6-54STU-321VW-X098Y', '2025-06-10', '2025-06-15', true, 53, 13),
('GHI12-3JKL4-56MNO-789PQR-S012T', '2025-07-15', '2025-05-30', false, 56, 1),
('VWX98-7YZT6-54ABC-321DEF-G098H', '2025-08-20', '2025-04-25', true, 59, 2),
('STU12-3VWX4-56XYZ-789ABC-D012E', '2025-09-25', '2025-03-20', false, 62, 3);