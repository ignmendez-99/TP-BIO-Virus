const blast_res_path = "output_files/resultados_blast";
const analysis_path = "output_files/resultado_analisis";

const fs = require("fs");
const path = require("path");

let csv = "id\thit_id\thit_title\thit_species\thit_evalue\thit_identity";

function main() {
    const files = JSON.parse(fs.readFileSync(path.join(blast_res_path, "resultado_blast.json")).toString()).BlastJSON;
    for (let f of files) {
        f = JSON.parse(fs.readFileSync(path.join(blast_res_path, f.File).replace("resultado_blast.json", "resultado_blast")).toString());

        const search_prefix = `${f.BlastOutput2.report.results.search.query_id.replace("Query_","")}`;
        for (const hit of f.BlastOutput2.report.results.search.hits) {
            let species = hit.description[0].title.match(/\[.*\]/ )
            species = species != null ? species[0].slice(1,species[0].length - 1) : "";

            csv += `\n${search_prefix}\t"${hit.description[0].id}"\t"${hit.description[0].title}"\t"${species}"\t${hit.hsps[0].evalue}\t${
                hit.hsps[0].identity / hit.len
            }`;
        }
        
    }

    fs.writeFileSync(path.join(analysis_path, "results.csv"), csv);
}


main();