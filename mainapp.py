@app.route("/search", methods=["POST"])
def search():
    gene = request.form["gene"]
    handle = Entrez.esearch(db="gene", term=gene, retmax=5)
    record = Entrez.read(handle)
    handle.close()
    
    ids = record["IdList"]
    results = []
    for gene_id in ids:
        summary= Entrez.esummary(db="gene",id=gene_id)
        data=Entrez.read(summary)
        gene_info =data["documentsummaryset"]["documentsummary"][0]

        results.apped({
            "name": gene_info["name"],