Aqui estamos criando um aplicativo de gestão/controle de finanças pessoais integrado com whatsapp

Comandos necessários para controle de versionamento no git:

COMANDOS QUE SÃO FEITOS APENAS UMA ÚNICA VEZ:
git init                    # ← Só na primeira vez do projeto
git config --global user.name "João"
git config --global user.email "seu@email.com"
git remote add origin https://github.com/...  # ← Só na primeira conexão

FLUXO NORMAL DO DIA A DIA:
-> Ao iniciar:
cd controle_gastos         # Entra na pasta do projeto
git status                 # (Opcional) Ver se está tudo ok
git pull                   # (Opcional) Baixa atualizações se houver

-> Durante o desenvolvimento:
# Você programa normalmente...
# Quando quiser salvar uma versão:

git add .
git commit -m "Implementa tal funcionalidade"
git push

-> Quando termina o dia:
git add .
git commit -m "Finaliza trabalho do dia"
git push


📊 COMANDOS PARA VER O ESTADO DO PROJETO:

bashgit status                  # Estado atual (arquivos modificados, etc.)  
git log                     # Histórico de commits  
git log --oneline          # Histórico resumido em uma linha  
git log --graph            # Histórico visual com branches  
git diff                   # Mostra exatamente o que mudou  
git diff arquivo.py        # Diferenças de um arquivo específico  

🔄 COMANDOS PARA GERENCIAR MUDANÇAS:

bashgit add arquivo.py         # Adiciona arquivo específico  
git add .                  # Adiciona todos os arquivos  
git add -A                 # Adiciona todos (incluindo deletados)  
git commit -m "mensagem"   # Commit com mensagem  
git commit -am "mensagem"  # Add + commit de arquivos já rastreados  

↩️ COMANDOS PARA DESFAZER COISAS:

bashgit checkout -- arquivo.py    # Desfaz mudanças não commitadas  
git reset HEAD arquivo.py     # Remove arquivo do staging  
git reset --soft HEAD~1       # Desfaz último commit (mantém mudanças)  
git reset --hard HEAD~1       # Desfaz último commit (perde mudanças)  
git revert HEAD               # Cria commit que desfaz o anterior  

🌐 COMANDOS PARA REPOSITÓRIO REMOTO:

bashgit push                   # Envia commits para GitHub  
git pull                   # Baixa atualizações do GitHub  
git clone URL              # Clona repositório existente  
git remote -v              # Mostra repositórios remotos conectados  
git fetch                  # Baixa info sem fazer merge  

🌳 COMANDOS PARA BRANCHES (ÚTIL QUANDO EVOLUIR):

bashgit branch                 # Lista branches locais  
git branch nova-feature    # Cria nova branch  
git checkout main          # Muda para branch main  
git checkout -b nova-feature  # Cria e muda para nova branch  
git merge nova-feature     # Faz merge da branch  
git branch -d nova-feature # Deleta branch  

🔍 COMANDOS PARA INVESTIGAÇÃO:

bashgit show                   # Mostra último commit detalhado  
git show HEAD~2            # Mostra commit de 2 versões atrás  
git blame arquivo.py       # Mostra quem fez cada linha  
git grep "texto"           # Busca texto nos arquivos  

⚠️ COMANDOS PARA SITUAÇÕES DE EMERGÊNCIA:

bashgit stash                  # Salva mudanças temporariamente  
git stash pop              # Recupera mudanças salvas  
git clean -f               # Remove arquivos não rastreados  
git reflog                 # Histórico de TUDO (para recuperar coisas)  

🏷️ COMANDOS PARA VERSÕES QUANDO O PROJETO CRESCER:

bashgit tag v1.0               # Cria tag para versão  
git tag                    # Lista tags  
git push --tags            # Envia tags para GitHub  

📝 COMANDOS MAIS USADOS NO DIA A DIA:

Para 90% do tempo:
bashgit status
git add .
git commit -m "mensagem"
git push
git pull
git log --oneline
Para quando algo der errado:
bashgit diff                   # "O que mudou?"
git checkout -- arquivo   # "Desfaz essa mudança"
git reset HEAD~1           # "Desfaz último commit"