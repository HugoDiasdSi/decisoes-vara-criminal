"""
Extração de texto de PDFs com suporte a OCR
"""

import PyPDF2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import io
import re


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrai texto de um arquivo PDF, usando OCR se necessário

    Args:
        pdf_path: Caminho para o arquivo PDF

    Returns:
        Texto extraído do PDF
    """
    text = ""

    try:
        # Tentar extração de texto nativo primeiro
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()

                if page_text and len(page_text.strip()) > 50:
                    # Página tem texto extraível
                    text += f"\n--- Página {page_num + 1} ---\n"
                    text += page_text
                else:
                    # Página pode ser digitalizada, tentar OCR
                    text += f"\n--- Página {page_num + 1} (OCR) ---\n"
                    ocr_text = extract_text_with_ocr(pdf_path, page_num)
                    text += ocr_text

    except Exception as e:
        # Se falhar, tentar OCR em todas as páginas
        print(f"Erro na extração nativa, tentando OCR: {e}")
        try:
            text = extract_all_pages_with_ocr(pdf_path)
        except Exception as ocr_error:
            text = f"Erro ao extrair texto: {str(ocr_error)}"

    # Limpar e formatar o texto
    text = clean_extracted_text(text)

    return text


def extract_text_with_ocr(pdf_path: str, page_num: int) -> str:
    """
    Extrai texto de uma página específica usando OCR

    Args:
        pdf_path: Caminho para o arquivo PDF
        page_num: Número da página (0-indexed)

    Returns:
        Texto extraído via OCR
    """
    try:
        # Converter página para imagem
        images = convert_from_path(
            pdf_path,
            first_page=page_num + 1,
            last_page=page_num + 1,
            dpi=300
        )

        if images:
            # Aplicar OCR na imagem
            text = pytesseract.image_to_string(
                images[0],
                lang='por',  # Português
                config='--psm 6'  # Assume uniform text block
            )
            return text
        return ""

    except Exception as e:
        return f"Erro no OCR da página {page_num + 1}: {str(e)}"


def extract_all_pages_with_ocr(pdf_path: str) -> str:
    """
    Extrai texto de todas as páginas usando OCR

    Args:
        pdf_path: Caminho para o arquivo PDF

    Returns:
        Texto extraído via OCR de todas as páginas
    """
    text = ""

    try:
        # Converter todas as páginas para imagens
        images = convert_from_path(pdf_path, dpi=300)

        for i, image in enumerate(images):
            text += f"\n--- Página {i + 1} (OCR) ---\n"

            # Aplicar OCR
            page_text = pytesseract.image_to_string(
                image,
                lang='por',
                config='--psm 6'
            )
            text += page_text

    except Exception as e:
        text = f"Erro ao processar PDF com OCR: {str(e)}"

    return text


def clean_extracted_text(text: str) -> str:
    """
    Limpa e formata o texto extraído

    Args:
        text: Texto bruto extraído

    Returns:
        Texto limpo e formatado
    """
    # Remover múltiplos espaços em branco
    text = re.sub(r'\s+', ' ', text)

    # Remover múltiplas quebras de linha
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)

    # Remover espaços no início e fim de linhas
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)

    return text.strip()


def extract_metadata_from_text(text: str) -> dict:
    """
    Extrai metadados do texto (IDs, números de processo, datas, etc.)

    Args:
        text: Texto extraído do PDF

    Returns:
        Dicionário com metadados extraídos
    """
    metadata = {
        'document_ids': [],
        'process_numbers': [],
        'dates': [],
        'cpf_cnpj': []
    }

    # Extrair IDs de documentos (ex: "ID 215703324", "Num. 170681275")
    id_patterns = [
        r'ID\s*(\d{6,})',
        r'Num\.\s*(\d{6,})',
        r'Id\s*Doc\s*(\d{6,})',
        r'Evento\s*(\d{6,})'
    ]

    for pattern in id_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        metadata['document_ids'].extend(matches)

    # Remover duplicatas
    metadata['document_ids'] = list(set(metadata['document_ids']))

    # Extrair números de processo (formato CNJ)
    process_pattern = r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}'
    metadata['process_numbers'] = re.findall(process_pattern, text)

    # Extrair datas (formato DD/MM/AAAA)
    date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
    metadata['dates'] = re.findall(date_pattern, text)

    # Extrair CPF/CNPJ
    cpf_pattern = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    cnpj_pattern = r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'
    metadata['cpf_cnpj'].extend(re.findall(cpf_pattern, text))
    metadata['cpf_cnpj'].extend(re.findall(cnpj_pattern, text))

    return metadata


def identify_document_sections(text: str) -> dict:
    """
    Identifica seções do documento (denúncia, depoimentos, laudos, etc.)

    Args:
        text: Texto do documento

    Returns:
        Dicionário com seções identificadas
    """
    sections = {}

    # Padrões para identificar seções
    section_patterns = {
        'denuncia': r'(DEN[ÚU]NCIA|INICIAL ACUSAT[ÓO]RIA)',
        'resposta_acusacao': r'(RESPOSTA [AÀ] ACUSA[ÇC][ÃA]O|DEFESA PR[ÉE]VIA)',
        'depoimento': r'(DEPOIMENTO|OITIVA|DECLARA[ÇC][ÕO]ES)',
        'laudo': r'(LAUDO|PER[ÍI]CIA|EXAME)',
        'mandado': r'(MANDADO DE|MANDATO)',
        'decisao': r'(DECIS[ÃA]O|DESPACHO|SENTEN[ÇC]A)',
        'certidao': r'(CERTID[ÃA]O|CERTIFICO)',
        'oficio': r'(OF[ÍI]CIO)'
    }

    for section_name, pattern in section_patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        positions = [match.start() for match in matches]
        if positions:
            sections[section_name] = positions

    return sections
