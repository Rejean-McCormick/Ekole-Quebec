"""Illustrative editorial writing for multiplication; explicitly not automatic generation."""
from .core import source_scaffold


def curated_multiplication(source):
    cid='qc-pri-ma-008'
    if source['course']['id']!=cid:raise ValueError('Le pilote ne concerne que qc-pri-ma-008')
    doc=source_scaffold(source,cid)
    # Activités formulées pour 8–9 ans. Aucune réponse à l'exercice diagnostique d'origine.
    texts=[
        ('Les groupes égaux',[
            ('explanation','Quand plusieurs groupes contiennent le même nombre d’objets, ce sont des groupes égaux.'),
            ('instruction','Prends des jetons ou dessine trois boîtes. Place quatre jetons dans chaque boîte.'),
            ('reflection','Est-ce que chaque boîte contient le même nombre de jetons ?')]),
        ('Je dessine une situation',[
            ('challenge','Une classe prépare trois boîtes avec quatre crayons dans chaque boîte. Dessine la situation sur une feuille.'),
            ('hint','Compte les crayons une boîte à la fois. Tu peux aussi utiliser des petits objets.'),
            ('reflection','Comment peux-tu montrer que les boîtes sont toutes pareilles ?')]),
        ('Je comprends la multiplication',[
            ('explanation','On peut additionner plusieurs fois le même nombre pour compter des groupes égaux. On peut aussi utiliser le signe ×.'),
            ('instruction','Imagine deux groupes de trois jetons. Écris une addition qui représente ton dessin.'),
            ('reflection','Combien de groupes as-tu faits ? Combien de jetons y a-t-il dans chaque groupe ?')]),
        ('Je m’exerce',[
            ('instruction','Ouvre l’activité de jetons du cours. Modifie les deux nombres et regarde les groupes changer.'),
            ('challenge','Essaie de créer cinq groupes de deux jetons, puis deux groupes de cinq jetons.'),
            ('reflection','Qu’est-ce qui reste pareil ? Qu’est-ce qui change ?')]),
        ('Une mission de livraison',[
            ('challenge','Une boulangerie prépare quatre plateaux avec trois petits pains sur chaque plateau. Dessine les plateaux.'),
            ('instruction','Cherche une addition qui correspond à ton dessin. Présente ta démarche à ton enseignant.'),
            ('hint','Commence par montrer un seul plateau, puis ajoute les autres.')]),
        ('Je fais le point',[
            ('reflection','Je sais montrer des groupes égaux avec des objets ou un dessin.'),
            ('reflection','Je peux expliquer comment je compte tous les objets.'),
            ('instruction','Montre ton dessin à un camarade ou à ton enseignant et explique comment tu as trouvé.')]),
    ]
    for m,(title,blocks) in zip(doc['modules'],texts):
        m['titre']=title
        m['blocks']=[{'type':kind,'text':text} for kind,text in blocks]
    doc['spek_candidate']={'historical_section_id':'week-10',
                           'historical_dataset_ref':'ekole-kontexte:qc3-stage2:candidate:1',
                           'link_status':'candidate_requires_teacher_review',
                           'note':'Correspondance possible avec la boulangerie, non certifiée.'}
    return doc
