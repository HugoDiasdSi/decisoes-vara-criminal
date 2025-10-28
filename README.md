METADADOS


{
  "paths": {
    "prompts_dir": "prompts",
    "base_conhecimento_dir": "base_conhecimento",
    "modelos_estilo_dir": "modelos_estilo",
    "cache_dir": ".cache/minutas",
    "minutas_metadata": "base_conhecimento/minutas_metadata.json"
  },
  "github": {
    "enabled": true,
    "repository": "HugoDiasdSi/decisoes-vara-criminal",
    "branch": "main",
    "cache_expiry_hours": 24,
    "excluded_files": ["README.md", "LICENSE", "config.json", ".gitignore"]
  },
  "prompts": {
    "extracao_flash": "prompts/extracao_flash.md",
    "extracao_flash_decisao": "prompts/extracao_flash_decisao.md",
    "assessor_juridico": "prompts/assessor_juridico.md",
    "elaborar_sentenca": "prompts/elaborar_sentenca.md",
    "formato_saida": "prompts/formato_saida_duplo.md"
  },
  "base_conhecimento": {
    "template": "base_conhecimento/TEMPLATE.md",
    "dosimetria": "base_conhecimento/Dosimetria RAG.md",
    "agente_rag": "base_conhecimento/Agente RAG.md",
    "anti_dupla_punicao": "base_conhecimento/ANTI-dupla punição pelo mesmo fato na dosimetria da pena.md",
    "orientacoes": "base_conhecimento/Orientações para a base de conhecimento.md"
  },
  "models": {
    "flash": "models/gemini-flash-lite-latest",
    "pro": "models/gemini-2.5-pro"
  },
  "generation_config": {
    "flash": {
      "temperature": 0.0
    },
    "pro": {
      "timeout": 600
    }
  },
  "ui": {
    "title": "Assessor Jurídico Virtual ⚖️",
    "theme": "soft"
  },
  "limits": {
    "max_pdf_size_mb": 10,
    "max_text_length": 50000
  }
}
