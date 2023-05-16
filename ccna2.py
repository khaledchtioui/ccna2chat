import difflib

# Define a dictionary with question-answer pairs
knowledge_base = {




    "Dans quelle situation un technicien utilise-t-il la commande de commutateur show interfaces ?": ["Lorsque des paquets sont reçus d’un hôte donné qui est directement connecté"],
    "Faites correspondre le numéro d’étape à la séquence des étapes qui se produisent pendant le processus de basculement HSRP. (Les propositions ne doivent pas être toutes utilisées.)": ["etape 1 :le routeur de transfert echoue","etape 2 : le routeur en veille cesse de voir les messages ","etape 3 : le routeur de secours assume le role"],
    "Reportez-vous à l’illustration. Un administrateur tente de configurer une route statique IPv6 sur le routeur R1 pour atteindre le réseau connecté au routeur R2. Après la saisie de la commande de la route statique, la connectivité au réseau est toujours défaillante. Quelle erreur a été effectuée dans la configuration de la route statique ?": ["L’interface est incorrecte."],
    "Un nouveau commutateur de couche 3 est connecté à un routeur et est en cours de configuration pour le routage InterVLAN. Quelles sont les trois étapes requises pour la configuration? (Choisissez trois propositions.)": ["Création d’interfaces SVI", "Activation du routage IP", "Attribution de ports aux VLAN"],
    "Reportez-vous à l’illustration. En fonction de la configuration et de la sortie présentées, pourquoi manque-t-il le VLAN 99 ?": ["Parce que le VLAN 99 n’a pas encore été créé"],
    "Quels sont les deux modes VTP qui permettent la création, la modification et la suppression des VLAN sur le commutateur local ? (Choisissez deux propositions.)": ["transparent", "serveur"],
    "Quelles paires de modes d’agrégation établissent une liaison agrégée fonctionnelle entre deux commutateurs Cisco ? (Choisissez trois réponses.)": ["dynamic desirable – dynamic auto", "dynamic desirable – trunk", "dynamic desirable – dynamic desirable"],
    "Quel protocole ou technologie nécessite que les commutateurs soient en mode serveur ou client?": ["Protocole VTP"],
    "Examinez l’illustration. Après avoir essayé de saisir la configuration affichée dans le routeur RTA, un administrateur reçoit une erreur et les utilisateurs du VLAN 20 signalent qu’ils ne peuvent pas communiquer avec les utilisateurs du VLAN 30. Quelle est l’origine du problème ?": ["RTA utilise le même sous-réseau pour le VLAN 20 et le VLAN 30."],
    "Reportez-vous à l’illustration. Un administrateur réseau configure R1 pour le routage inter-VLAN entre VLAN 10 et VLAN 20. Toutefois, les périphériques du VLAN 10 et du VLAN 20 ne peuvent pas communiquer. Selon la configuration de l’exposition, quelle est la cause possible du problème?": ["La commande interface gigabitEthernet 0/0.1 est faux."],
    "Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur utiliserait-il un contrôleur WLAN?": ["pour faciliter la configuration de groupe et la gestion de plusieurs WLAN via un WLC"],
    "Associez la description au type de VLAN correct. (Les options ne sont pas toutes utilisées.)": ["vlan par defaut => tous les ports de commutateur sont attribués", "reseau locaux virtuels ==> une addresse ip et un masque de sous reseau sont attreibué", "reseaux locaux virtuels vlan de sonnés ==> configuration destinee a acheminer le trafic","ressau local virtuel vlan natif==> acheminement du trafic non etiqueté"],
    "Examinez l’illustration. Comment une trame envoyée depuis PCA est-elle transmise à PCC si la table d’adresses MAC du commutateur SW1 est vide ?": ["SW1 diffuse la trame sur tous les ports de SW1, à l’exception du port d’entrée de la trame dans le commutateur."],
    "Associez l’état de la liaison au statut d’interface et de protocole. (Les options ne sont pas toutes utilisées.)": ["desacativé ==>desactivé par un administrateur", "prbleme de couche 1 ==> down/down", "prbleme de couche 1 ==> up/down","opérationel==> up/up"],
    "Quel est le moyen d’avoir une configuration sécurisée pour l’accès à distance à un appareil sur le réseau ?": ["Configurer SSH."],
    "Reportez-vous à l’illustration. Quels sont les rôles possibles pour les ports A, B, C et D dans ce réseau RSTP ?": ["Alternatif, désigné, racine, racine"],
    "Plusieurs actions peuvent pallier une attaque de VLAN. Citez-en trois. (Choisissez trois propositions.)": ["Activer manuellement le trunking.","Faire d’un VLAN inutilisé le VLAN natif.","Désactiver le protocole DTP."],
    "Quelle méthode de chiffrement sans fil offre la meilleure sécurité ?": ["WPA2 avec AES"],
    "Après qu’un hôte a généré une adresse IPv6 à l’aide du processus DHCPv6 ou SLAAC, comment l’hôte vérifie-t-il que l’adresse est unique et donc utilisable?": ["L’hôte envoie un message de sollicitation de voisin ICMPv6 à l’adresse DHCP ou SLAAC apprise et si aucune annonce de voisin n’est renvoyée, l’adresse est considérée comme unique."],
    "Un administrateur tente de supprimer des configurations d’un commutateur. Après avoir exécuté la commande erase startup-config et rechargé le commutateur, l’administrateur constate que les VLAN 10 et 100 existent toujours dans le commutateur. Pourquoi ces VLAN n’ont-ils pas été supprimés ?": ["Ces VLAN étant enregistrés dans un fichier appelé vlan.dat qui se trouve dans la mémoire Flash, ce fichier doit être supprimé manuellement."],
    "Examinez l’illustration. Un administrateur réseau configure le routage inter-VLAN sur un réseau. Pour l’instant, un seul VLAN est utilisé, mais d’autres seront ajoutés prochainement. Quel est le rôle du paramètre manquant, indiqué par un point d’interrogation mis en surbrillance dans l’illustration ?": ["Il identifie le numéro du VLAN."],
    "Après avoir attaché quatre PC aux ports du commutateur, configuré le SSID et défini les propriétés d’authentification pour un petit réseau de bureau, un technicien teste avec succès la connectivité de tous les PC connectés au commutateur et au WLAN. Un pare-feu est ensuite configuré sur le périphérique avant de le connecter à Internet. Quel type de périphérique réseau inclut toutes les fonctionnalités décrites?": ["routeur sans fil"],
    "Associez les types de message DHCP à l’ordre du processus DHCPv4. (Les options ne doivent pas être toutes utilisées.)": ["etape1 => dhcpdiscover ","etape2 => dhcpoffer","etape3 => dhcprequest","etape4 => dhcpack"],
    "Examinez l’illustration. En plus des routes statiques qui dirigent le trafic vers les réseaux 10.10.0.0/16 et 10.20.0.0/16, le routeur HQ est configuré avec la commande suivante : ip route 0.0.0.0 0.0.0.0 serial 0/1/1": ["Les paquets dont le réseau de destination n’est ni 10.10.0.0/16 ni 10.20.0.0/16, ou dont le réseau de destination n’est pas connecté directement seront transférés à Internet."],
    "Examinez l’illustration. Quelle adresse MAC de destination est utilisée lorsque des trames sont envoyées depuis la station de travail vers la passerelle par défaut ?": ["L’adresse MAC du routeur virtuel"],
    "Reportez-vous à l’illustration. Un administrateur réseau a relié deux commutateurs via la technologie EtherChannel. Si le protocole STP fonctionne, quel sera le résultat final ?": ["STP bloquera une des liaisons redondantes."],
    "Reportez-vous à l’illustration. Quelle route statique un technicien informatique doit-il saisir pour créer une route de secours vers le réseau 172.16.1.0 qui sera utilisée uniquement en cas de défaillance de la route principale associée à RIP ?": ["ip route 172.16.1.0 255.255.255.0 s0/0/0 121"],
    "Quel est l’effet de l’entrée de la commande de configuration shutdown sur un commutateur?": ["Il désactive un port inutilisé."],
    "Quelles sont les trois normes Wi-Fi fonctionnant dans la plage de fréquences 2,4 GHz ? (Choisissez trois réponses.)": ["802.11b","802.11n","802.11g"],
    "Un technicien réseau dépanne un réseau sans fil venant d’être déployé et utilisant les normes 802.11 les plus récentes. Lorsque les utilisateurs accèdent à des services gourmands en bande passante tels que la vidéo sur Internet, les performances du réseau sans fil sont médiocres. Pour améliorer les performances, le technicien réseau décide de configurer un SSID avec une bande de fréquences de 5 GHz et de former les utilisateurs à employer ce SSID pour les services multimédias de transmission en continu. En quoi cette solution permet-elle d’améliorer les performances du réseau sans fil pour ce type de service ?": ["La bande 5 GHz offre davantage de canaux et est moins encombrée que la bande 2,4 GHz. Elle convient donc mieux à la transmission multimédia en continu."],
    "Sélectionnez les trois modes d’établissement de canaux PAgP. (Choisissez trois propositions.)": ["Activé","desirable","automatique"],
    "Reportez-vous à l’illustration. L’administrateur réseau est en train de configurer la fonction de sécurité du port sur le commutateur SWC. L’administrateur a émis la commande show port-security interface fa 0/2 pour vérifier la configuration. Que peut-on conclure de la sortie qui est montrée? (Choisissez trois propositions.)": ["Les violations de sécurité entraîneront l’arrêt immédiat de ce port.","Ce port est actuellement en service.","Le mode de port de commutation pour cette interface est le mode d’accès."],
    "Quel protocole doit être désactivé pour pallier les attaques de VLAN ?": ["DTP"],
    "Quelle technique d’atténuation empêcherait les serveurs malveillants de fournir de faux paramètres de configuration IP aux clients ?": ["activation de l’espionnage DHCP"],
    "Quelle méthode d’attribution de préfixe IPv6 repose sur le préfixe contenu dans les messages RA?": ["SLAAC"],
    "Un analyste de la cybersécurité utilise l’outil macof pour évaluer la configuration des commutateurs déployés dans le réseau de base d’une organisation. Quel type d’attaque LAN l’analyste cible-t-il au cours de cette évaluation?": ["Débordement de la table d’adresses IP"],
    "Au cours du processus AAA, quand l’autorisation est-elle implémentée ?": ["immédiatement après une authentification réussie auprès d’une source de données AAA"],
    "Examinez l’illustration. Un ingénieur réseau configure le routage IPv6 sur le réseau. Quelle commande exécutée sur le routeur HQ permet de configurer une route par défaut vers Internet en vue de transférer les paquets vers un réseau de destination IPv6 qui n’est pas répertorié dans la table de routage ?​": ["ipv6 route ::/0 serial 0/1/1"],
    "Quel type de route statique est configuré avec une plus grande distance administrative pour fournir une route de secours vers une route associée à un protocole de routage dynamique ? ": ["route statique flottante"],
    "Quelle réponse indique une route statique par défaut IPv4 correctement configurée ?": ["ip route 0.0.0.0 0.0.0.0 S0/0/0"],
    "Reportez-vous à l’illustration. Quelle commande de route statique peut être entrée sur R1 pour transférer le trafic vers le réseau local connecté à R2?": ["ipv6 route 2001:db8:12:10::/64 S0/0/1 fe80::2"],
    "Examinez l’illustration. Quelle métrique permet de transférer un paquet de données avec l’adresse de destination IPv6 2001:DB8:ACAD:E:240:BFF:FED4:9DD2 ?": ["2682112"],
    "Reportez-vous à l’illustration. Le routeur R1 a une relation de voisin OSPF avec le routeur ISP sur le réseau 192.168.0.32. La liaison réseau 192.168.0.36 doit servir de sauvegarde lorsque la liaison OSPF tombe en panne. La commande flottante statique route ip route 0.0.0.0 0.0.0.0 S0/0/1 100 a été émise sur R1 et maintenant le trafic utilise la liaison de sauvegarde même lorsque la liaison OSPF est en service. Quelle modification doit être apportée à la commande route statique afin que le trafic n’utilise la liaison OSPF que lorsqu’elle est en service?": ["Modifiez la distance administrative sur 120."],
    "Reportez-vous à l’illustration. Quelle route a été configurée comme route statique vers un réseau spécifique en utilisant l’adresse du tronçon suivant ?": ["S 10.17.2.0/24 [1/0] via 10.16.2.2"],
    "Reportez-vous à l’illustration. Quel trunk ne transmettra aucun trafic au terme du processus de sélection de pont racine ?": ["Trunk2"],
    "Quels sont les deux types de protocoles STP pouvant générer des flux de trafic non optimaux parce qu’ils ne supposent qu’une seule instance Spanning Tree pour le réseau ponté entier ? (Choisissez deux réponses.)": ["STP","RSTP"],
    "Pour obtenir un aperçu de l’état du mode Spanning Tree d’un réseau commuté, un technicien réseau exécute la commande show spanning-tree sur un commutateur. Quelles informations cette commande permet-elle d’afficher ? (Choisissez deux réponses.)": ["L’ID de pont racine.","Le rôle des ports sur tous les VLAN."],
    "Examinez l’illustration. Quelles sont les deux conclusions pouvant être tirées du résultat ? (Choisissez deux réponses.)": ["L’ID de canal de port correspond à 2.","La liaison EtherChannel est en panne."],
    "Quelle action se déroule lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination monodiffusion apparaissant dans la table d’adresses MAC?": ["Le commutateur transmet le cadre hors du port spécifié."],
    "Reportez-vous à l’illustration. Un administrateur réseau a ajouté un nouveau sous-réseau au réseau et veut que les hôtes du sous-réseau reçoivent des adresses IPv4 du serveur DHCPv4.Quelles commandes permettent aux hôtes du nouveau sous-réseau de recevoir des adresses du serveur DHCPv4 ? (Choisissez deux réponses.)": ["R1(config)# interface G0/0","R1(config-if)# ip helper-address 10.2.0.250"],
    "Quelle action prend un client DHCPv4 s’il reçoit plus d’un DHCPOFFER de plusieurs serveurs DHCP?": ["Il envoie un DHCPREQUEST qui identifie l’offre de location que le client accepte."],
    "Examinez l’illustration. Si les adresses IP du routeur de passerelle par défaut et du serveur de noms de domaine (DNS) sont correctes, quel est le problème de cette configuration ?": ["L’adresse IP du routeur de passerelle par défaut ne figure pas dans la liste d’adresses exclues."],
    "Les utilisateurs de la succursale ont pu accéder à un site le matin, mais n’ont pas eu de connectivité avec le site depuis l’heure du déjeuner. Que faut-il faire ou vérifier?": ["Utilisez la commande « show ip interface brief » pour voir si une interface est en panne."],
    "Associez la caractéristique de transmission à son type. (Les options ne sont pas toutes utilisées.)": ["1)convient aux application informatiques hautement ==> cut-through cible 1","2)controle les erreurs avant la transmission ==> store-and forward cible 1","3)le processus  de transmision peut démarrer des la  ==> cut-through cible 2","4)le processus de transmision peut demarrer uniquement apres avoir ==> store-and forward cible 2","5)les trames non valodes peuvent etre transmises  ==> cut-through cible 3","6)seules les trames valides sont transmises==> store-and forward cible 2"],
    "Quelles informations un commutateur utilise-t-il pour renseigner la table d’adresses MAC ?": ["l’adresse MAC source et le port entrant"],
    "Pour quelles raisons un administrateur réseau segmenterait-il un réseau avec un commutateur de couche 2 ? (Choisissez deux réponses.)": ["Pour isoler le trafic entre les segments.","Pour améliorer la bande passante utilisateur."],
    "Un technicien dépannage un WLAN lent et décide d’utiliser l’approche de répartition du trafic. Quels deux paramètres devraient être configurés pour le faire? (Choisissez deux propositions.)": ["Configurez la bande 2,4 GHz pour le trafic Internet de base qui n’est pas sensible au temps.","Configurez la bande 5 GHz pour le streaming multimédia et le trafic temporel."],
    "Sur un Cisco 3504 WLC Summary page ( Advanced > Summary ), quel onglet permet à un administrateur réseau de configurer un WLAN particulier avec une stratégie WPA2?": ["Réseaux locaux sans fil"],
    "Un administrateur réseau ajoute un nouveau WLAN sur un WLC Cisco 3500. Quel onglet l’administrateur doit-il utiliser pour créer une nouvelle interface VLAN à utiliser pour le nouveau WLAN?": ["CONTRÔLEUR"],
    "Quel est l’effet de l’entrée de la commande de configuration switchport mode access sur un commutateur?": ["Il désactive le PAO sur une interface non-trunking."],
    "Reportez-vous à l’illustration. L’administrateur réseau configure les deux commutateurs comme illustré. Cependant, l’hôte C ne peut envoyer de requête ping à l’hôte D et l’hôte E ne peut envoyer de requête ping à l’hôte F. Quelle action l’administrateur doit-il effectuer pour activer cette communication ?": ["Configurer un port trunk en mode dynamic desirable."],
    "Associez l’étape à la description de la séquence d’amorçage du commutateur correspondante. (Les options ne doivent pas être toutes utilisées.)": ["etape3=>initialations du registre du processur","etape 1=>execution du post","etape 4=>Initialisation du systeme de fichiers flash","etape 2=>Chargement du programme d'amorcage a parir de la memoire morte (rom)","etape 5=>Charger le logiciel Ios","etape 6=>controle de la commutation de tranfer a l'ios   "],
    "Reportez-vous à l’illustration. Supposons que le courant vient juste d’être rétabli. PC3 émet une requête de diffusion DHCP IPv4. À quel port SW1 transmet-il cette requête ?": ["À Fa0/1, à Fa0/2 et à Fa0/3 uniquement"],
    "Quel préfixe IPv6 est conçu pour la communication lien-local?": ["fe80::/10"],
    "Comment un routeur gère-t-il le routage statique si Cisco Express Forwarding est désactivé": ["Les interfaces Ethernet à accès multiple nécessitent des routes statiques entièrement spécifiées pour éviter des incohérences au niveau du routage."],
    "Reportez-vous à l’illustration. Que peut-on conclure de la configuration affichée sur R1?": ["Configurez R1 en tant qu’agent de relais DHCP."],
    "Quelle action se déroule lorsque l’adresse MAC source d’un cadre entrant dans un commutateur n’est pas dans la table d’adresses MAC?": ["Le commutateur ajoute à la table l’adresse MAC et le numéro de port entrant."],
    "Le routage inter-VLAN réussi fonctionne depuis un certain temps sur un réseau avec plusieurs VLAN sur plusieurs commutateurs. Lorsqu’une liaison de jonction entre commutateurs échoue et que le protocole Spanning Tree affiche une liaison de jonction de sauvegarde, il est signalé que les hôtes de deux VLAN peuvent accéder à certaines ressources réseau, mais pas à toutes les ressources précédemment accessibles. Les hôtes sur tous les autres VLAN n’ont pas ce problème. Quelle est la cause la plus probable de ce problème?": ["La fonction de port de bord protégé sur les interfaces de jonction de sauvegarde a été désactivée."],
    "Un administrateur réseau utilise le modèle « Router-on-a-Stick » pour configurer un commutateur et un routeur pour le routage inter-VLAN. Comment le port du commutateur connecté au routeur doit-il être configuré ?": ["Il doit être configuré comme port agrégé 802.1q."],
    "Pourquoi l’espionnage DHCP est-il nécessaire lors de l’utilisation de la fonction Dynamic ARP Inspection?": ["Il utilise la base de données de liaison d’adresse MAC à adresse IP pour valider un paquet ARP."],
    "Reportez-vous à l’illustration. Un administrateur réseau a configuré les routeurs R1 et R2 comme faisant partie du groupe HSRP 1. Après le rechargement des routeurs, un utilisateur associé à l’hôte 1 s’est plaint d’une mauvaise connectivité à Internet. L’administrateur réseau a donc exécuté la commande show standby brief sur les deux routeurs pour vérifier le fonctionnement du protocole HSRP. En outre, l’administrateur a observé le tableau ARP sur Host1. Quelle entrée doit apparaître dans le tableau ARP sur Host1 pour acquérir la connectivité à Internet?": ["L’adresse IP virtuelle et l’adresse MAC virtuelle du groupe HSRP 1"],
    "Une route statique a été configurée sur un routeur. Cependant, le réseau de destination n’existe plus. Que doit faire un administrateur pour supprimer l’itinéraire statique de la table de routage ?": ["Supprimez l’itinéraire en utilisant la commande no ip route ."],
    "Un technicien junior ajoutait un itinéraire à un routeur LAN. Un traceroute vers un périphérique sur le nouveau réseau a révélé un mauvais chemin et un état inaccessible. Que faut-il faire ou vérifier?": ["Vérifiez la configuration de l’interface de sortie sur la nouvelle route statique."],
    "Quelle méthode d’authentification sans fil dépend d’un serveur d’authentification RADIUS ?": ["WPA2 Enterprise"],
    "Quels sont les deux paramètres définis par défaut sur un routeur sans fil pouvant affecter la sécurité du réseau ? (Choisissez deux propositions.)": ["Le SSID est diffusé.","Un mot de passe administrateur réservé est défini."],
    "Un administrateur réseau d’une petite société de publicité configure la sécurité WLAN à l’aide de la méthode PSK WPA2. Quelles informations d’identification les utilisateurs de bureau ont-ils besoin pour connecter leurs ordinateurs portables au WLAN?": ["Phrase secrète de l’utilisateur"],
    "Quelle commande permet de créer une route statique sur R2 pour atteindre PC B ?": ["R2(config)# ip route 172.16.2.0 255.255.255.0 172.16.3.1"],
    "Reportez-vous à l’illustration. R1 a été configuré avec la commande de route statique ip route 209.165.200.224 255.255.255.224 S0/0/0 et, par conséquent, les utilisateurs du réseau 172.16.0.0/16 ne peuvent pas accéder aux ressources sur Internet. Comment cette route statique doit-elle être modifiée pour permettre au trafic utilisateur du LAN d’accéder à Internet ?": ["En configurant le réseau et le masque de destination sur 0.0.0.0 0.0.0.0."],
    "Quel est le risque associé à la méthode de la base de données locale pour la sécurisation de l’accès des appareils qui peut être réalisée au moyen de AAA sur des serveurs centralisés ?": ["Les comptes des utilisateurs doivent être configurés localement sur chaque appareil, ce qui est une solution d’authentification non évolutive."],
    "Quel protocole ou technologie utilise l’adresse IP source vers l’adresse IP de destination comme mécanisme d’équilibrage de charge?": ["EtherChannel   "],
    "Examinez l’illustration. Tous les commutateurs affichés sont des modèles Cisco 2960 dont la priorité par défaut est identique et fonctionnant à la même bande passante. Quels sont les trois ports qui seront désignés pour STP ? (Choisissez trois réponses.)": ["Fa0/10","Fa0/21","Fa0/13"],
    "Un ingénieur WLAN déploie un WLC et cinq points d’accès sans fil à l’aide du protocole CAPWAP avec la fonction DTLS pour sécuriser le plan de contrôle des périphériques réseau. Lors du test du réseau sans fil, l’ingénieur WLAN remarque que le trafic de données est en cours d’échange entre le WLC et les AP en texte brut et qu’il n’est pas crypté. Quelle est la raison la plus probable pour cela?": ["Bien que DTLS soit activé par défaut pour sécuriser le canal de contrôle CAPWAP, il est désactivé par défaut pour le canal de données."],
    "Contrairement aux routes dynamiques, quels sont les avantages qu’offre l’utilisation des routes statiques sur un routeur ? (Choisissez deux réponses.)": ["Elles utilisent moins de ressources du routeur.","Elles améliorent la sécurité du réseau."],
    "Examinez l’illustration. R1 a été configuré comme illustré. Cependant, PC1 ne parvient pas à recevoir d’adresse IPv4. Quel est le problème ?": ["La commande ip helper-address n’a pas été exécutée sur l’interface correcte."],
    "Quel est l’effet de l’entrée de la commande de configuration ip arp inspection vlan 10 sur un commutateur?": ["Il active le DAI sur des interfaces de commutation spécifiques précédemment configurées avec la surveillance DHCP."],
    "Quelle action se déroule lorsque l’adresse MAC source d’un cadre entrant dans un commutateur apparaît dans la table d’adresses MAC associée à un port différent?": ["Le commutateur remplace l’ancienne entrée et utilise le port le plus courant."],
    "Reportez-vous à l’illustration. Actuellement, le routeur R1 utilise une route EIGRP enregistrée via Branch2 pour atteindre le réseau 10.10.0.0/16. Quelle route statique flottante crée une route de secours vers le réseau 10.10.0.0/16 au cas où la liaison entre R1 et Branch2 serait interrompue ?": ["ip route 10.10.0.0 255.255.0.0 209.165.200.225 100"],
    "Quelles sont les trois étapes à suivre avant de transférer un commutateur Cisco vers un nouveau domaine de gestion VTP ? (Choisissez trois réponses.)": ["Redémarrer le commutateur.","Configurer le commutateur avec le nom du nouveau domaine de gestion.","Sélectionner le mode et la version VTP appropriés."],
    "Reportez-vous à l’illustration. Quelle opération effectue le routeur R1 sur un paquet associé à une adresse IPv6 de destination 2001:db8:cafe:5::1 ?": ["ransmettre le paquet en sortie sur Serial0/0/0"],
    "Quelle est la principale raison pour un cybercriminel de lancer une attaque par dépassement d’adresses MAC ?": ["pour que le cybercriminel puisse voir les trames destinées à d’autres hôtes"],
    "Quelle proposition décrit le résultat de l’interconnexion de plusieurs commutateurs Cisco LAN ?": ["Le domaine de diffusion s’étend sur tous les commutateurs."],
    "Reportez-vous à l’illustration. Un administrateur réseau configure le routeur R1 pour l’attribution d’adresse IPv6. Sur la base de la configuration partielle, quel système d’attribution d’adresses IPv6 global monodiffusion l’administrateur a-t-il l’intention de mettre en œuvre ?": ["avec état (stateful)"],
    "Examinez l’illustration. Un administrateur réseau vérifie la configuration du commutateur S1. Quel protocole a été implémenté pour regrouper plusieurs ports physiques en une liaison logique ?": ["PAgP"],
    "Une politique de sécurité de l’entreprise exige que l’adressage MAC soit enregistré de manière dynamique et ajouté à la table des adresses MAC et à la configuration en cours sur chaque commutateur. Quelle configuration de la sécurité des ports permettra de respecter cette mesure ?": ["adresses MAC sécurisées fixes"],
    "Un administrateur réseau utilise la commande de configuration globale spanning-tree portfastbpduguard default pour activer la garde BPDU sur un commutateur. Cependant, BPDU guard n’est pas activé sur tous les ports d’accès. Quelle est la source du problème?": ["PortFast n’est pas configuré sur tous les ports d’accès."],
    "Examinez l’illustration. Un commutateur de couche 3 se charge du routage pour trois VLAN et se connecte à un routeur pour la connectivité Internet. Comment le commutateur doit-il être configuré ? (Choisissez deux réponses.)": ["(config)# ip routing","(config)# interface gigabitethernet 1/1(config-if)# no switchport(config-if)# ip address 192.168.1.2 255.255.255.252"],
    "Quel est l’effet de l’entrée de la commande de configuration ip dhcp snooping sur un commutateur?": ["Activez globalement la surveillance DHCP (snooping )sur le commutateur."],
    "Un administrateur réseau est en train de configurer un WLAN. Pourquoi l’administrateur désactiverait-il la fonction de diffusion pour le SSID?": ["pour éliminer l’analyse des SSID disponibles dans la zone"],
    "Une entreprise déploie un réseau sans fil dans le site de distribution d’une banlieue de Boston. L’entrepôt est assez volumineux et nécessite l’utilisation de plusieurs points d’accès. Étant donné que certains appareils de l’entreprise fonctionnent toujours à 2,4 GHz, l’administrateur réseau décide de déployer la norme 802.11g. Quels sont les canaux que vous affecterez aux différents points d’accès afin d’éviter les chevauchements ?": ["Canaux 1, 6 et 11"],
    "Quelle attaque a pour but de créer un DOS pour les clients en les empêchant d’obtenir un crédit-bail DHCP ?": ["Insuffisance de ressources DHCP"],
    "Les utilisateurs d’un réseau local ne peuvent pas accéder à un serveur Web d’entreprise mais peuvent se rendre ailleurs. Que faut-il faire ou vérifier?": ["Vérifiez que la route statique vers le serveur est présente dans la table de routage."],
    "Quelle commande permet de lancer le processus de regroupement de deux interfaces physiques afin de créer un groupe EtherChannel par le biais du protocole LACP ?": ["interface range GigabitEthernet 0/4 – 5"],
    "Quelle instruction est correcte sur la façon dont un commutateur de couche 2 détermine comment transférer des trames?": ["Les décisions de transfert de trame sont basées sur l’adresse MAC et les mappages des ports dans la table CAM."],
    "Reportez-vous à l’illustration. Quels sont les trois hôtes qui recevront des requêtes ARP de l’hôte A, dans l’hypothèse où le port Fa0/4 sur les deux commutateurs est configuré pour transporter du trafic pour plusieurs VLAN ? (Choisissez trois réponses.)": ["hôte F","hôte C","hôte D"],
    "Parmi les propositions suivantes, lesquelles caractérisent les ports routés d’un commutateur multicouche ? Choisissez deux réponses.": ["Ils ne sont associés à aucun VLAN particulier."],
    
    "Un administrateur réseau prépare l’implémentation du protocole Rapid PVST+ sur un réseau de production. Comment les types de liaisons Rapid PVST+ sont-ils déterminés sur les interfaces de commutateur ?": ["Les types de liaisons sont déterminés automatiquement."],
    "Sur quels ports de commutation devrait-on activer la protection BPDU pour améliorer la stabilité STP?": ["tous les ports équipés de PortFast"],

    "Quelle est une méthode pour lancer une attaque par saut de VLAN ?":["\nintroduction d’un commutateur non autorisé et activation de la jonction"] ,
    "Examinez l’illustration. Un administrateur réseau configure un routeur en tant que serveur DHCPv6. L’administrateur émet une commande show ipv6 dhcp pool pour vérifier la configuration. Quelle affirmation explique la raison pour laquelle le nombre de clients actifs est de 0 ?":["\nL’état n’est pas maintenu par le serveur DHCPv6 dans le cadre d’une opération DHCPv6 sans état."] ,
    "Examinez l’illustration. En plus des routes statiques dirigeant le trafic vers les réseaux 10.10.0.0/16 et 10.20.0.0/16, Router HQ est également configuré avec la commande suivante :ip route 0.0.0.0 0.0.0.0 série 0/1/1":["\nPaquets avec unle réseau de destination qui n’est pas 10.10.0.0/16 ou qui n’est pas 10.20.0.0/16 ou qui n’est pas un réseau directement connecté sera transféré vers Internet."] ,
    "Quel protocole ou quelle technologie désactive les chemins redondants pour éliminer les boucles de couche 2 ?":["\nSTP"] ,
    "Quel est l’effet de la saisie de la commande de configuration spanning-tree portfast sur un commutateur ?":["\nIl active le portfast sur une interface de commutateur spécifique."] ,
    "Quel est le préfixe IPv6 utilisé pour les adresses lien-local ?":["\nFE80::/10"] ,
    "Quelle action a lieu lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination de multidiffusion ?":["\nLe commutateur transférera la trame vers tous les ports à l’exception du port entrant." ],
    "Un technicien junior ajoutait une route vers un routeur LAN. Une traceroute vers un périphérique sur le nouveau réseau a révélé un chemin erroné et un statut inaccessible. Que faut-il faire ou vérifier ?":["\nVérifiez la configuration de l’interface de sortie sur la nouvelle route statique."] ,
    "Quel est le terme commun donné aux messages de journal SNMP générés par les périphériques réseau et envoyés au serveur SNMP ?":["\npièges" ],
    "Un administrateur réseau configure un WLAN. Pourquoi l’administrateur modifierait-il les adresses DHCP IPv4 par défaut sur un point d’accès ?":["\npour réduire l’interception des données ou l’accès au réseau sans fil par des personnes extérieures en utilisant une plage d’adresses bien connue" ],
    "Quelles sont les deux fonctions exécutées par un WLC lors de l’utilisation du contrôle d’accès aux médias (MAC) ? (Choisissez deux réponses.)":["\nassociation et réassociation de clients itinérants\ntraduction du cadre vers d’autres protocoles" ],
    "Quelle attaque réseau est atténuée en activant la protection BPDU ?":["\ncommutateurs indésirables sur un réseau" ],
    "Un administrateur réseau configure un nouveau commutateur Cisco pour l’accès à la gestion à distance. Quels sont les trois éléments à configurer sur le commutateur pour la tâche ? (Choisissez trois réponses.)":["\nAdresse IP\nlignes vty\npasserelle par défaut" ],
    "Examinez l’illustration. Quelle déclaration affichée dans la sortie permet au routeur R1 de répondre aux requêtes DHCPv6 sans état ?":["\nipv6 et other-config-flag​" ],
    "Une entreprise vient de passer à un nouveau FAI. Le FAI a terminé et vérifié la connexion de son site à l’entreprise. Cependant, les employés de l’entreprise ne peuvent pas accéder à Internet. Que faut-il faire ou vérifier ?":["\nAssurez-vous que l’ancienne route par défaut a été supprimée des routeurs périphériques de l’entreprise."] ,
    "Quel protocole ou quelle technologie permet aux données de transmettre sur des liaisons de commutation redondantes ?":["\nSTP" ],
    "Quels sont les deux protocoles utilisés pour fournir une authentification AAA basée sur le serveur ? (Choisissez deux réponses.)":["\nTACACS+\nRAYON"] ,
    "Quelle technique d’atténuation empêcherait les serveurs malveillants de fournir de faux paramètres de configuration IP aux clients ?":["\nactivation de la surveillance DHCP" ],
    "Un administrateur réseau configure la fonction de sécurité des ports sur un commutateur. La politique de sécurité spécifie que chaque port d’accès doit autoriser jusqu’à deux adresses MAC. Lorsque le nombre maximum d’adresses MAC est atteint, une trame avec l’adresse MAC source inconnue est supprimée et une notification est envoyée au serveur syslog. Quel mode de violation de sécurité doit être configuré pour chaque port d’accès ?":["\nrestreindre"] ,
    "Un technicien configure un routeur pour une petite entreprise avec plusieurs WLAN et n’a pas besoin de la complexité d’un protocole de routage dynamique. Qu’est-ce que doitêtre fait ou vérifié ?":["\nCréez des routes statiques vers tous les réseaux internes et une route par défaut vers Internet."] ,
    "Quel plan d’atténuation est le meilleur pour contrecarrer une attaque DoS qui crée un débordement de table d’adresses MAC ?":["\nActiver la sécurité des ports." ],
    "Quel message DHCPv4 un client enverra-t-il pour accepter une adresse IPv4 proposée par un serveur DHCP ?":["\ndiffusion DHCPREQUEST"] ,
    "Faites correspondre le but avec son type de message DHCP. (Toutes les options ne sont pas utilisées.)":["\na message that is used to locate any avaliableDHCP server on a network->DHCPDICOVER\na message that is used to idnetify the explicit server...->DHCPREQUEST\na message that is used to acknowledge...->DHCPPACK\na message that is used to suggest a lease..->DHCPOFFER\n" ],
    "Quel protocole ajoute de la sécurité aux connexions à distance ?":["\nSSH"] ,
    "Examinez l’illustration. Un administrateur réseau vérifie la configuration du routage inter-VLAN. Les utilisateurs se plaignent que PC2 ne peut pas communiquer avec PC1. Sur la base de la sortie, quelle est la cause possible du problème ?":["\nLe eLa commande ncapsulation dot1Q 5 contient le mauvais VLAN." ],
    "Faites correspondre chaque type de message DHCP avec sa description. (Toutes les options ne sont pas utilisées.)":["\nDHCPPACK->the dhcp server confirming that the..\nDHCPREQUEST->the client acceptingthe IP..\nDHCPDISCOVER->a client intiating a message to find..\nDHCPOFFER->a DHCP server responding to the ..\n"] ,
    "Quelle attaque réseau cherche à créer un DoS pour les clients en les empêchant d’obtenir un bail DHCP ?":["\nFamine DHCP" ],
    "Quelle commande permettra à un routeur de commencer à envoyer des messages lui permettant de configurer une adresse lien-local sans utiliser de serveur DHCP IPv6 ?":["\nla commande ipv6 unicast-routing" ],
    "Un administrateur réseau a trouvé un utilisateur envoyant une trame 802.1Q doublement marquée à un commutateur. Quelle est la meilleure solution pour empêcher ce type d’attaque ?":["\nLes VLAN pour les ports d’accès utilisateur doivent être des VLAN différents de tous les VLAN natifs utilisés sur les ports de jonction." ],
    "Les utilisateurs se plaignent d’un accès sporadique à Internet chaque après-midi. Que faut-il faire ou vérifier ?":["\nVérifiez les statistiques sur la route par défaut pour la sursaturation." ],
    "Un nouveau commutateur de couche 3 est connecté à un routeur et est en cours de configuration pour le routage interVLAN. Quelles sont trois des cinq étapes requises pour la configuration ? (Choisissez trois réponses.)":["\nCas 1 :\ncréation de VLAN\nattribution de ports aux VLAN\ncréation d’interfaces SVI \n\nCas 2 :\nactivation du routage IP\nen saisissant « pas de port de commutation » sur le port connecté au routeur\nattribution de ports aux VLAN\n\nCas 3 :\nactivation du routage IP\nen saisissant « pas de port de commutation » sur le port connecté au routeur\nétablissement de contiguïtés"] ,
    "Quelles sont les trois déclarations qui décrivent avec précision les paramètres de duplex et de vitesse sur les commutateurs Cisco 2960 ? (Choisissez trois réponses.)":["\nUn échec de négociation automatique peut entraîner des problèmes de connectivité.\nLorsque la vitesse est définie sur 1000 Mb/s, les ports du commutateur fonctionnent en mode duplex intégral.\nLes paramètres de duplex et de vitesse de chaque port de commutateur peuvent être configurés manuellement."] ,
    "Un nouveau commutateur doit être ajouté à un réseau existant dans un bureau distant. L’administrateur réseau ne souhaite pas que les techniciens du bureau distant puissent ajouter de nouveaux VLAN au commutateur, mais le commutateur doit recevoir les mises à jour VLAN du domaine VTP. Quelles sont les deux étapes à effectuer pour configurer VTP sur le nouveau commutateur afin de répondre à ces conditions ? (Choisissez deux réponses.)":["\nConfigurez le nouveau commutateur en tant que client VTP.\nConfigurez le nom de domaine VTP existant sur le nouveau commutateur." ],
    "Les employés ne peuvent pas se connecter aux serveurs sur l’un des réseaux internes. Que faut-il faire ou vérifier ?":["\nUtilisez la commande “show ip interface brief” pour voir si une interface est en panne."] ,
    "Un administrateur remarque qu’un grand nombre de paquets sont supprimés sur l’un des routeurs de succursale. Que faut-il faire ou vérifier ?":["\nVérifiez la table de routage pour une route statique manquante." ],
    "Quelles sont les deux caractéristiques du commutateur qui pourraient aider à réduire la congestion du réseau ? (Choisissez deux réponses.)":["\ncommutation interne rapide\ntampons de grande taille"] ,
    "Quel est le résultat de la connexion de deux ou plusieurs commutateurs ensemble ?":["\nLa taille du domaine de diffusion est augmentée." ],
    "Quel est l’effet de la saisie de la commande de configuration switchport port-security sur un commutateur ?":["\nIl active la sécurité des ports sur une interface." ],
    "Un administrateur réseau configure un WLAN. Pourquoi l’administrateur utiliserait-il plusieurs points d’accès légers ?":["\npour faciliter la configuration et la gestion de groupe de plusieurs WLAN via un WLC" ],
    "Examinez l’illustration. PC-A et PC-B sont tous deux dans le VLAN 60. PC-A est incapable de communiquer avec PC-B. Quel est le problème ?":["\nLe VLAN utilisé par PC-A ne figure pas dans la liste des VLAN autorisés sur le tronc." ],
    "Un administrateur réseau configure un WLAN. Pourquoi l’administrateur utiliserait-il des serveurs RADIUS sur le réseau ?":["\npour restreindre l’accès au WLAN uniquement aux utilisateurs autorisés et authentifiés" ],
    "Un administrateur réseau a configuré un routeur pour un fonctionnement DHCPv6 sans état. Cependant, les utilisateurs signalent que les postes de travail ne reçoivent pas les informations du serveur DNS. Quelles lignes de configuration de routeur doivent être vérifiées pour s’assurer que le service DHCPv6 sans état est correctement configuré ? (Choisissez deux réponses.)":["\nLa ligne DNS-server est incluse dans la section ipv6 dhcp pool.\nLe ipv6 nd other-config-flag est saisi pour l’interface qui fait face au segment LAN."] ,
    "Quelle action a lieu lorsqu’une trame entrant dans un commutateur a une adresse MAC de destination de monodiffusion qui ne figure pas dans la table d’adresses MAC ?":["\nLe commutateur transférera la trame vers tous les ports à l’exception du port entrant." ],
    "Quel protocole ou quelle technologie gère les négociations de jonction entre les commutateurs ?":["\nDTP"] ,
    "Un administrateur réseau configure un WLAN. Pourquoi l’administrateur appliquerait-il WPA2 avec AES au WLAN ?":["\npour assurer la confidentialité et l’intégrité du trafic sans fil en utilisant le cryptage" ],
    "Quel est l’effet de la saisie de la commande de configuration ip dhcp snooping limit rate 6 sur un commutateur ?":["\nIl restreint le nombre de messages de découverte, par seconde, à recevoir sur l’interface."] ,
    "Un administrateur réseau configure un WLAN. Pourquoi l’administrateur modifierait-il les adresses DHCP IPv4 par défaut sur un point d’accès ?":["\npour réduire l’interception des données ou l’accès au réseau sans fil par des personnes extérieures en utilisant une plage d’adresses bien connue" ],
    "Quel est l’effet de la saisie de la commande de configuration ip arp inspection validate src-mac sur un commutateur ?":["\nIl vérifie l’adresse L2 source dans l’en-tête Ethernet par rapport à l’adresse L2 de l’expéditeur dans le corps ARP." ],
    "Quel protocole ou quelle technologie est un protocole propriétaire Cisco qui est automatiquement activé sur les commutateurs 2960 ?":["\nDTP" ],
    "Quelle longueur d’adresse et de préfixe est utilisée lors de la configuration d’une route statique IPv6 par défaut ?":["\n::/0" ],
    "Quelles sont les deux caractéristiques de Cisco Express Forwarding (CEF) ? (choisitet deux.)":["\nIl s’agit du mécanisme de transfert le plus rapide sur les routeurs Cisco et les commutateurs multicouches.\nLes paquets sont transférés en fonction des informations contenues dans le FIB et d’un tableau de contiguïté." ],
    "Quel terme décrit le rôle d’un commutateur Cisco dans le contrôle d’accès basé sur les ports 802.1X ?":["authentificateur" ],
    "Quelle solution Cisco permet d’éviter les attaques d’usurpation d’identité ARP et d’empoisonnement ARP ?":["\nInspection ARP dynamique" ],
    "Quel est l’avantage de PVST+ ?":["\nPVST+ optimise les performances sur le réseau grâce au partage de charge."] ,
    "Quel protocole ou quelle technologie utilise un routeur de secours pour assumer la responsabilité du transfert de paquets si le routeur actif tombe en panne ?":["\nHSRP" ],
    "Quel est l’effet de la saisie de la commande de configuration show ip dhcp snooping binding sur un commutateur ?":["\nIl affiche les associations d’adresses IP vers MAC pour les interfaces de commutateur." ],
    "Quelle action a lieu lorsque l’adresse MAC source d’une trame entrant dans un commutateur est dans la table d’adresses MAC ?":["\nLe commutateur met à jour la minuterie d’actualisation de l’entrée." ],
    "Une petite maison d’édition a une conception de réseau telle que lorsqu’une diffusion est envoyée sur le réseau local, 200 appareils reçoivent la diffusion transmise. Comment l’administrateur réseau peut-il réduire le nombre d’appareils recevant du trafic de diffusion ?":["\nSegmentez le réseau local en réseaux locaux plus petits et acheminez entre eux.*" ],
    "Qu’est-ce qui définit une route hôte sur un routeur Cisco ?":["\nUne configuration de route hôte statique IPv4 utilise une adresse IP de destination d’un appareil spécifique et un masque de sous-réseau /32." ],
    "Quoi d’autre est requis lors de la configuration d’une route statique IPv6 à l’aide d’une adresse lien-local de prochain saut ?":["\nnuméro et type d’interface" ],
    "Un technicien configure un réseau sans fil pour une petite entreprise à l’aide d’un routeur sans fil SOHO. Quelles sont les deux méthodes d’authentification utilisées si le routeur est configuré avec WPA2 ? (Choisissez deux réponses.)":["\npersonnel\nentreprise" ],
    "Un PC a envoyé un message RS à un routeur IPv6 connecté au même réseau. Quelles sont les deux informations que le routeur enverra au client ? (Choisissez deux réponses.)":["\nlongueur du préfixe\npréfixe" ],
    "Lorsqu’ils assistent à une conférence, les participants utilisent des ordinateurs portables pour la connectivité réseau. Lorsqu’un orateur invité tente de se connecter au réseau, l’ordinateur portable ne parvient pas à afficher les réseaux sans fil disponibles. Le point d’accès doit fonctionner dans quel mode ?":["\nactif" ],
    "Quels sont les trois composants combinés pour former un identifiant de pont ?":["\nID système étendu\npriorité du pont\nAdresse MAC" ],


  
  
    # Add more question-answer pairs here
}

# Function to prompt for a question and pr
# ovide an answer
def prompt_for_question():
    question = input("Please enter your question: ")
    return question

# Function to print text in color
def print_color(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
    print(colors[color] + text + colors["reset"])

# Function to find partial matches in the knowledge base
def find_partial_matches(question):
    matches = difflib.get_close_matches(question, knowledge_base.keys(), n=1, cutoff=0.6)
    return matches

# Main script
while True:
    user_question = prompt_for_question()

    if user_question.lower() == "exit":
        print("Exiting...")
        break

    user_question_lower = user_question.lower()

    if user_question_lower in knowledge_base:
        answers = knowledge_base[user_question_lower]
        print_color("Answers:", "green")
        for answer in answers:
            print(answer)
    else:
        matches = find_partial_matches(user_question_lower)
        if matches:
            if matches[0].lower() == user_question_lower:
                answers = knowledge_base[matches[0]]
                print_color("Answers:", "green")
                for answer in answers:
                    
                    print_color(answer, "green")
            else :
                if len(matches)==1 :
                    answers = knowledge_base[matches[0]]
                    print_color("Answers:", "green")
                    for answer in answers:
                    
                         print_color(answer, "green")
                else:
                         
                    print_color("Did you mean one of these?", "yellow")
                    for match in matches:
                        print(match)
                        print_color("+++++++++++","yellow")
        else:
            words = user_question_lower.split()
            suggestions = []
            for key in knowledge_base.keys():
                key_words = key.lower().split()
                if all(word in key_words for word in words):
                    suggestions.append(key)
            if suggestions:
                if len(suggestions)==1 :
                    print_color("Did you mean one of these?", "yellow")
                    print(suggestions[0])

                    
                    answers = knowledge_base[suggestions[0]]
                    print_color("Answers:", "green")
                    for answer in answers:
                         print_color(answer, "green")
                else :
                     print_color("Did you mean one of these?", "yellow")
                    
                     for suggestion in suggestions:
                           print(suggestion)
                           print_color("-------------------", "yellow")
            else:
                print_color("I'm sorry, I don't know the answer to that question.", "red")
