INSERT INTO tarefa (nomeTarefa, descricao, categoria, dataPrazo, prioridade, status)
VALUES
('Trabalho de História',
'Capítulo 4 e resumo de 2 páginas',
'Escola', '2026-12-10', 'ALTA', 'Pendente'),

('Organizar o quarto',
'Arrumar a mesa e organizar os materiais',
'Pessoal', '2026-12-12', 'BAIXA', 'Pendente'),

('Projeto de Programação',
'Finalizar o código e testar as funcionalidades',
'Curso', '2026-12-15', 'ALTA', 'Em andamento'),

('Revisar conteúdo de Biologia',
'Estudar células e organelas para a avaliação',
'Escola', '2026-12-09', 'MEDIA', 'Pendente'),

('Atualizar currículo',
'Adicionar cursos e projetos recentes',
'Pessoal', '2026-12-20', 'MEDIA', 'Pendente');

SELECT * FROM tarefa;
