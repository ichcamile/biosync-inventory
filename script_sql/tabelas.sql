CREATE DATABASE IF NOT EXISTS biosync_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biosync_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    perfil ENUM('admin', 'comum') NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    quantidade_minima INT NOT NULL
);

CREATE TABLE IF NOT EXISTS movements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    tipo ENUM('entrada', 'saida') NOT NULL,
    quantidade INT NOT NULL,
    data_movimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES products(id)
);


INSERT INTO products (nome, quantidade, quantidade_minima) VALUES
('Paracetamol 500mg', 100, 20),
('Ibuprofeno 400mg', 80, 15),
('Dipirona 1g', 120, 30),
('Amoxicilina 500mg', 50, 10),
('Azitromicina 500mg', 60, 12),
('Omeprazol 20mg', 70, 15),
('Losartana 50mg', 40, 8),
('Metformina 850mg', 90, 20),
('Cloridrato de Sertralina 50mg', 30, 6),
('Enalapril 10mg', 45, 9),
('Loratadina 10mg', 100, 20),
('Ranitidina 150mg', 55, 10),
('Diclofenaco 50mg', 60, 12),
('Cetirizina 10mg', 80, 15),
('Cloridrato de Fluoxetina 20mg', 35, 7),
('Nimesulida 100mg', 75, 15),
('Clonazepam 2mg', 25, 5),
('Prednisona 20mg', 30, 6),
('Hidroclorotiazida 25mg', 50, 10),
('Cloridrato de Ciprofloxacino 500mg', 40, 8),
('Alprazolam 0,5mg', 30, 5),
('AAS 100mg', 100, 20),
('Cetoconazol 20mg', 45, 8),
('Salbutamol 100mcg', 60, 12),
('Furosemida 40mg', 50, 10),
('Risperidona 2mg', 30, 6),
('Cloridrato de Amitriptilina 25mg', 20, 5),
('Dexametasona 4mg', 40, 8),
('Fenitoína 100mg', 35, 7),
('Glimepirida 4mg', 60, 12),
('Hidroclorotiazida 12,5mg', 50, 10),
('Metoprolol 50mg', 45, 9),
('Cloridrato de Diazepam 5mg', 30, 6),
('Norfloxacino 400mg', 40, 8),
('Rosuvastatina 10mg', 50, 10),
('Cloridrato de Sertralina 100mg', 25, 5),
('Cloridrato de Fluoxetina 40mg', 30, 6),
('Losartana Potássica 100mg', 50, 10),
('Doxiciclina 100mg', 45, 8),
('Cloridrato de Amoxicilina 875mg', 60, 12),
('Lansoprazol 30mg', 50, 10),
('Bromoprida 10mg', 40, 8),
('Ácido Acetilsalicílico 300mg', 60, 12),
('Levofloxacino 500mg', 50, 10);

INSERT INTO users (nome, username, senha, perfil) VALUES
('Administrador BioSync', 'admin', '$2b$12$KIXQyPVXq5IkZqipkZq9KuPqY0WmMYaZ9hd0wTfDQ0tXmmOdCmwWq', 'admin');
