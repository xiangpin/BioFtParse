import pandas as pd

def diffdict_df(dicts):
    newda = dict([(k, pd.Series("; ".join(v))) if isinstance(v, list) and len(v) > 1 \
                    else (k, pd.Series(v[0])) if isinstance(v, list) and len(v) ==1 \
                    else (k, pd.Series(str(v))) \
                    for k, v in dicts.items()])
    newda = pd.DataFrame(newda)
    return (newda)

def extract_cds_annot(seqrecord):
    tmpgene = []
    for gene in seqrecord.features:
        if gene.type == "CDS":
            tmpquali = dict(gene.qualifiers)
            tmpquali = diffdict_df(tmpquali)
            tmpgene.append(tmpquali)
    if (len(tmpgene)>1):
        genes = pd.concat(tmpgene, sort=False)
        genes.insert(loc=0, column='SeqID', value=seqrecord.id)
        return (genes)

def extract_seq_annot(seqrecord):
    if isinstance(seqrecord.annotations["organism"], list):
        tmporganism = seqrecord.annotations["organism"][0]
    else:
        tmporganism = str(seqrecord.annotations["organism"])
    seqrecord.annotations["taxonomy"].append(tmporganism)
    if "references" in seqrecord.annotations:
        del seqrecord.annotations["references"]
    if "structured_comment" in seqrecord.annotations:
        del seqrecord.annotations["structured_comment"]
    if "comment" in seqrecord.annotations:
        del seqrecord.annotations["comment"]
    annotda = diffdict_df(seqrecord.annotations)
    annotda.insert(loc=0, column="SeqID", value=seqrecord.id)
    return (annotda)
