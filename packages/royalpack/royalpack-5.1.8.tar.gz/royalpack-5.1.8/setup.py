# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['royalpack',
 'royalpack.commands',
 'royalpack.events',
 'royalpack.stars',
 'royalpack.tables',
 'royalpack.utils']

package_data = \
{'': ['*']}

install_requires = \
['riotwatcher>=2.7.1,<3.0.0',
 'royalnet[telegram,discord,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]>=5.1.6,<6.0.0',
 'royalspells>=3.2,<4.0']

setup_kwargs = {
    'name': 'royalpack',
    'version': '5.1.8',
    'description': 'A Royalnet command pack for the Royal Games community',
    'long_description': "<!--This documentation was autogenerated with `python -m royalnet.generate -f markdown`.-->\n\n# `royalpack`\n\n## Commands\n\n### `ciaoruozi`\n\nSaluta Ruozi, un leggendario essere che una volta era in User Games.\n\n### `color`\n\nInvia un colore in chat...?\n\n### `cv`\n\nElenca le persone attualmente connesse alla chat vocale.\n\n### `diario`\n\nAggiungi una citazione al Diario.\n\n### `rage`\n\nArrabbiati per qualcosa, come una software house californiana.\n\n> Aliases: `balurage` `madden` \n\n### `reminder`\n\nTi ricorda di fare qualcosa dopo un po' di tempo.\n\n> Aliases: `calendar` \n\n### `ship`\n\nCrea una ship tra due nomi.\n\n### `smecds`\n\nSecondo me, è colpa dello stagista...\n\n> Aliases: `secondomeecolpadellostagista` \n\n### `videochannel`\n\nConverti il canale vocale in un canale video.\n\n> Aliases: `golive` `live` `video` \n\n### `pause`\n\nMetti in pausa o riprendi la riproduzione di un file.\n\n> Aliases: `resume` \n\n### `play`\n\nAggiunge un url alla coda della chat vocale.\n\n> Aliases: `p` \n\n### `queue`\n\nVisualizza la coda di riproduzione attuale..\n\n> Aliases: `q` \n\n### `skip`\n\nSalta il file attualmente in riproduzione.\n\n> Aliases: `s` \n\n### `summon`\n\nEvoca il bot in un canale vocale.\n\n> Aliases: `cv` \n\n### `youtube`\n\nCerca un video su YouTube e lo aggiunge alla coda della chat vocale.\n\n> Aliases: `yt` \n\n### `soundcloud`\n\nCerca un video su SoundCloud e lo aggiunge alla coda della chat vocale.\n\n> Aliases: `sc` \n\n### `emojify`\n\nConverti un messaggio in emoji.\n\n### `leagueoflegends`\n\nConnetti un account di League of Legends a un account Royalnet, e visualizzane le statistiche.\n\n> Aliases: `lol` `league` \n\n### `diarioquote`\n\nCita una riga del diario.\n\n> Aliases: `dq` `quote` `dquote` \n\n### `peertube`\n\nGuarda quando è uscito l'ultimo video su RoyalTube.\n\n### `googlevideo`\n\nCerca un video su Google Video e lo aggiunge alla coda della chat vocale.\n\n> Aliases: `gv` \n\n### `yahoovideo`\n\nCerca un video su Yahoo Video e lo aggiunge alla coda della chat vocale.\n\n> Aliases: `yv` \n\n### `userinfo`\n\nVisualizza informazioni su un utente.\n\n> Aliases: `uinfo` `ui` `useri` \n\n### `spell`\n\nGenera casualmente una spell!\n\n### `ahnonlosoio`\n\nAh, non lo so io!\n\n### `eat`\n\nMangia qualcosa!\n\n### `pmots`\n\nConfondi Proto!\n\n## Events\n\n### `discord_cv`\n\n### `discord_summon`\n\n### `discord_play`\n\n### `discord_skip`\n\n### `discord_queue`\n\n### `discord_pause`\n\n## Page Stars\n\n### `/api/user/list`\n\n### `/api/user/get/{uid_str}`\n\n### `/api/diario/list`\n\n### `/api/diario/get/{diario_id}`\n\n## Exception Stars\n\n## Tables\n\n### `diario`\n\n### `aliases`\n\n### `wikipages`\n\nWiki page properties.\n\n    Warning:\n        Requires PostgreSQL!\n\n### `wikirevisions`\n\nA wiki page revision.\n\n    Warning:\n        Requires PostgreSQL!\n\n### `bios`\n\n### `reminder`\n\n### `triviascores`\n\n### `mmevents`\n\n### `mmresponse`\n\n### `leagueoflegends`\n\n",
    'author': 'Stefano Pigozzi',
    'author_email': 'ste.pigozzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Steffo99/royalpack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
