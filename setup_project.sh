#!/bin/bash

# Nome do diretório raiz
root_dir="simulado_cisco"

# Estrutura de diretórios
dirs=(
    "$root_dir/app"
    "$root_dir/app/templates"
    "$root_dir/app/static"
    "$root_dir/app/static/css"
    "$root_dir/app/static/js"
)

# Arquivos a serem criados
files=(
    "$root_dir/app/main.py"
    "$root_dir/app/models.py"
    "$root_dir/app/database.py"
    "$root_dir/app/templates/base.html"
    "$root_dir/app/templates/index.html"
    "$root_dir/app/templates/question.html"
    "$root_dir/app/templates/result.html"
    "$root_dir/app/static/css/styles.css"
    "$root_dir/app/static/js/scripts.js"
    "$root_dir/questions.db"
    "$root_dir/requirements.txt"
    "$root_dir/README.md"
)

# Criar diretórios
for dir in "${dirs[@]}"; do
    mkdir -p "$dir"
    echo "Created directory: $dir"
done

# Criar arquivos vazios
for file in "${files[@]}"; do
    touch "$file"
    echo "Created file: $file"
done

echo "Estrutura do projeto '$root_dir' criada com sucesso."
