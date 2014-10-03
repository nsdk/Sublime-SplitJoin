sublime -> tools -> new plugin
colar o código do arquivo JoinSplit.py e salvar

depois abrir o arquivo Default.sublime-commands que ficam em:
preferences -> browser packages -> Default
e adicionar as seguintes propriedades:

    { "caption": "LG Join selected lines", "command": "lg_joinsel" },
    { "caption": "LG Join trim selected lines", "command": "lg_joinseltrim" },
    { "caption": "LG Remover espacos extras", "command": "lg_removerespacos" },
    { "caption": "LG Remover quebras de linhas extras", "command": "lg_removerquebras" },
    { "caption": "LG Agrupar", "command": "lg_removerrepetidos" },
    { "caption": "LG Agrupar com count", "command": "lg_agruparcount" },
    { "caption": "LG Split", "command": "lg_splitsel" }

agora é só chamar o command pallete (ctrl + shift + P), que os comandos estarão disponiveis

