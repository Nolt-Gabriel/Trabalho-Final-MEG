#!/bin/bash

#Esse Script atualiza as branchs locais, trazendo as branchs remotas
#Utilize quando você não estiver vendo as branchs remotas no local
#Para usar executar, digite no terminal: chmod -x ./branch.sh , para tornar o arquivo executável
#Depois basta digitar ./branch.sh no terminal que ele executará o Script

echo "<<<<< Script de Branchs >>>>>"
echo "<<<<<    By Noltuser    >>>>>"   
echo ""
echo ">Esse Script vai atualizar as branchs locais e sincronizar"
echo ">com as branchs remotas"
echo ""
read -p "Deseja continuar? (s/n): " resposta

if [[ $resposta == "s" || $resposta == "S" ]]; then
    echo "Continuando o script..."
    git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
    git fetch --all
    git pull --all

else
    echo "Script interrompido."
    exit 0
fi

