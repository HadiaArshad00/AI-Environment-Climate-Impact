"""
Report Builder Module
=====================
Builds professional academic Word documents with embedded figures,
tables, and formatted text.
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from pathlib import Path
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class ReportBuilder:
    """Builds professional academic Word documents."""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.font_name = 'Times New Roman'
        self.table_header_color = '1F4E79'
        logger.info("ReportBuilder initialized")

    def build(self, data: Dict, results: Dict, figures: List[str],
              title: str, author: str, date: str) -> str:
        """Build the complete research document."""
        doc = Document()
        self._setup_document(doc)
        self._build_title_page(doc, title, author, date)
        self._build_table_of_contents(doc)
        self._build_abstract(doc)
        self._build_chapter1_introduction(doc)
        self._build_chapter2_environmental_footprint(doc, data, figures)
        self._build_chapter3_mitigation(doc, data, figures)
        self._build_chapter4_jevons(doc, data, figures)
        self._build_chapter5_regulatory(doc, data)
        self._build_chapter6_sustainable_ai(doc, data)
        self._build_chapter7_outlook(doc)
        self._build_chapter8_conclusion(doc)
        self._build_references(doc)
        self._build_appendices(doc, data)

        filepath = self.output_dir / "AI_Environment_Climate_Change_Review.docx"
        doc.save(str(filepath))
        return str(filepath)

    def _setup_document(self, doc: Document):
        """Configure document-level settings."""
        style = doc.styles['Normal']
        style.font.name = self.font_name
        style.font.size = Pt(12)

        for level, size in [(1, 18), (2, 14), (3, 12)]:
            heading = doc.styles[f'Heading {level}']
            heading.font.name = self.font_name
            heading.font.size = Pt(size)
            heading.font.bold = True
            heading.font.color.rgb = RGBColor(0, 51, 102)
            heading.paragraph_format.space_before = Pt(12)
            heading.paragraph_format.space_after = Pt(6)

    def _add_para(self, doc, text, size=12, justify=True):
        p = doc.add_paragraph()
        if justify:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run = p.add_run(text)
        run.font.name = self.font_name
        run.font.size = Pt(size)
        return p

    def _add_fig_caption(self, doc, text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.italic = True
        run.font.size = Pt(10)
        run.font.name = self.font_name

    def _add_table(self, doc, title, headers, rows, note=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.bold = True
        run.font.name = self.font_name
        run.font.size = Pt(11)

        table = doc.add_table(rows=len(rows)+1, cols=len(headers))
        table.style = 'Table Grid'
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

        for i, h in enumerate(headers):
            cell = table.rows[0].cells[i]
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = cell.paragraphs[0].add_run(h)
            run.bold = True
            run.font.name = self.font_name
            run.font.size = Pt(10)
            shading = OxmlElement('w:shd')
            shading.set(qn('w:fill'), self.table_header_color)
            cell._tc.get_or_add_tcPr().append(shading)
            for r in cell.paragraphs[0].runs:
                r.font.color.rgb = RGBColor(255, 255, 255)

        for i, rd in enumerate(rows):
            for j, v in enumerate(rd):
                cell = table.rows[i+1].cells[j]
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = cell.paragraphs[0].add_run(v)
                run.font.name = self.font_name
                run.font.size = Pt(10)

        if note:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(note)
            run.italic = True
            run.font.size = Pt(9)
            run.font.name = self.font_name

    def _build_title_page(self, doc, title, author, date):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(24)
        run.font.name = self.font_name
        run.font.color.rgb = RGBColor(0, 51, 102)
        for _ in range(3): doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("A Comprehensive Review of Environmental Footprints,\nMitigation Strategies, and Sustainable Pathways")
        run.italic = True
        run.font.size = Pt(14)
        run.font.name = self.font_name
        for _ in range(4): doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(date)
        run.font.size = Pt(12)
        run.font.name = self.font_name
        doc.add_page_break()

    def _build_table_of_contents(self, doc):
        doc.add_heading('TABLE OF CONTENTS', level=1)
        doc.add_paragraph()
        toc = [
            ('Abstract','iii'),('1. Introduction','1'),('   1.1 Background and Context','1'),
            ('   1.2 Scope and Objectives','3'),('   1.3 Methodology','4'),
            ('2. The Environmental Footprint of Artificial Intelligence','5'),('   2.1 Energy Consumption in AI Training','5'),
            ('   2.2 Energy Consumption in AI Inference','8'),('   2.3 Water Consumption and Thermal Management','10'),
            ('   2.4 Carbon Emissions and Greenhouse Gas Impact','12'),('   2.5 Electronic Waste and Hardware Lifecycle','15'),
            ('   2.6 Rare Earth Mineral Extraction','17'),('3. AI in Climate Change Mitigation','19'),
            ('   3.1 Renewable Energy Optimization','19'),('   3.2 Smart Grid Management','22'),
            ('   3.3 Carbon Capture and Storage','25'),('   3.4 Precision Agriculture','27'),
            ('   3.5 Climate Modeling and Prediction','29'),('   3.6 Transportation and Logistics Optimization','31'),
            ('4. The Jevons Paradox and Rebound Effects','33'),('   4.1 Efficiency Gains vs. Demand Growth','33'),
            ('   4.2 Case Studies in AI-Induced Demand','35'),('5. Regulatory Frameworks and Policy Responses','37'),
            ('   5.1 European Union Regulations','37'),('   5.2 United States Policy Landscape','39'),
            ('   5.3 China and Asia-Pacific Initiatives','41'),('   5.4 International Standards and Guidelines','43'),
            ('6. Sustainable AI: Strategies and Best Practices','45'),('   6.1 Green Data Center Design','45'),
            ('   6.2 Carbon-Aware Computing','47'),('   6.3 Model Efficiency and Optimization','49'),
            ('   6.4 Hardware Innovation','51'),('   6.5 Circular Economy for AI Hardware','53'),
            ('7. Future Outlook and Recommendations','55'),('   7.1 Projected Trends (2026-2035)','55'),
            ('   7.2 Research Priorities','57'),('   7.3 Policy Recommendations','59'),
            ('8. Conclusion','61'),('References','63'),('Appendix A: Data Tables','78'),('Appendix B: Glossary of Terms','82'),
        ]
        tt = doc.add_table(rows=len(toc), cols=2)
        tt.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i,(s,p) in enumerate(toc):
            cl = tt.rows[i].cells[0]
            cr = tt.rows[i].cells[1]
            cl.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = cl.paragraphs[0].add_run(s)
            r.font.name = self.font_name
            r.font.size = Pt(11 if not s.startswith('   ') else 10)
            r.bold = not s.startswith('   ')
            cr.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r = cr.paragraphs[0].add_run(p)
            r.font.name = self.font_name
            r.font.size = Pt(11 if not s.startswith('   ') else 10)
            r.bold = not s.startswith('   ')
        for row in tt.rows:
            for cell in row.cells:
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcBorders = OxmlElement('w:tcBorders')
                for bn in ['top','left','bottom','right','insideH','insideV']:
                    b = OxmlElement(f'w:{bn}')
                    b.set(qn('w:val'),'none')
                    b.set(qn('w:sz'),'0')
                    b.set(qn('w:space'),'0')
                    b.set(qn('w:color'),'auto')
                    tcBorders.append(b)
                tcPr.append(tcBorders)
        doc.add_page_break()

    def _build_abstract(self, doc):
        doc.add_heading('ABSTRACT', level=1)
        self._add_para(doc, "The rapid proliferation of artificial intelligence (AI) technologies has precipitated an unprecedented surge in computational demand, fundamentally reshaping the global energy landscape and presenting both formidable environmental challenges and transformative climate mitigation opportunities.", 11)
        p = doc.add_paragraph()
        r = p.add_run('Keywords: ')
        r.bold = True
        r.font.name = self.font_name
        r.font.size = Pt(11)
        r = p.add_run('Artificial intelligence, climate change, data centers, carbon footprint, renewable energy, smart grid, sustainability, Jevons paradox, green computing, environmental policy')
        r.font.name = self.font_name
        r.font.size = Pt(11)
        doc.add_page_break()

    def _build_chapter1_introduction(self, doc):
        doc.add_heading('1. INTRODUCTION', level=1)
        doc.add_heading('1.1 Background and Context', level=2)
        self._add_para(doc, "The convergence of artificial intelligence and environmental sustainability represents one of the most consequential technological and ecological challenges of the 21st century.")
        doc.add_page_break()

    def _build_chapter2_environmental_footprint(self, doc, data, figures):
        doc.add_heading('2. THE ENVIRONMENTAL FOOTPRINT OF ARTIFICIAL INTELLIGENCE', level=1)
        doc.add_heading('2.1 Energy Consumption in AI Training', level=2)
        self._add_para(doc, "The training phase of large AI models represents one of the most energy-intensive computational tasks ever undertaken by humanity.")
        self._add_table(doc, 'Table 1: Energy Consumption and Carbon Emissions for Representative AI Model Training',
            ['Model', 'Parameters', 'Training Energy (MWh)', 'CO2 Emissions (tCO2e)', 'Year'],
            [['GPT-3','175B','1,287','552','2020'],['GPT-4','Est. 1.8T','50,000','~8,000','2023'],
             ['LLaMA 3.1 405B','405B','~30,000','~5,500','2024'],['Gemini Ultra','Est. 1.5T','~45,000','~7,200','2024'],
             ['Claude 3 Opus','Est. 500B','~20,000','~3,500','2024'],['Mistral Large 2','Est. 120B','~5,000','~900','2024']],
            'Note: Estimates vary by methodology. CO2 figures assume average US grid carbon intensity.')
        doc.add_page_break()

    def _build_chapter3_mitigation(self, doc, data, figures):
        doc.add_heading('3. AI IN CLIMATE CHANGE MITIGATION', level=1)
        doc.add_heading('3.1 Renewable Energy Optimization', level=2)
        self._add_para(doc, "The integration of variable renewable energy sources into electrical grids presents one of the most significant technical challenges of the energy transition.")
        doc.add_page_break()

    def _build_chapter4_jevons(self, doc, data, figures):
        doc.add_heading('4. THE JEVONS PARADOX AND REBOUND EFFECTS', level=1)
        doc.add_heading('4.1 Efficiency Gains vs. Demand Growth', level=2)
        self._add_para(doc, "The Jevons Paradox, first observed by William Stanley Jevons in 1865 regarding coal consumption, posits that improvements in resource efficiency can increase total resource consumption.")
        doc.add_page_break()

    def _build_chapter5_regulatory(self, doc, data):
        doc.add_heading('5. REGULATORY FRAMEWORKS AND POLICY RESPONSES', level=1)
        doc.add_heading('5.1 European Union Regulations', level=2)
        self._add_para(doc, "The European Union has emerged as the global leader in AI environmental regulation.")
        doc.add_page_break()

    def _build_chapter6_sustainable_ai(self, doc, data):
        doc.add_heading('6. SUSTAINABLE AI: STRATEGIES AND BEST PRACTICES', level=1)
        doc.add_heading('6.1 Green Data Center Design', level=2)
        self._add_para(doc, "The design and operation of data centers fundamentally determines the environmental footprint of AI computing.")
        doc.add_page_break()

    def _build_chapter7_outlook(self, doc):
        doc.add_heading('7. FUTURE OUTLOOK AND RECOMMENDATIONS', level=1)
        doc.add_heading('7.1 Projected Trends (2026-2035)', level=2)
        self._add_para(doc, "The trajectory of AI's environmental impact over the next decade will be shaped by the interplay of technological innovation, market dynamics, regulatory pressure, and societal choices.")
        doc.add_page_break()

    def _build_chapter8_conclusion(self, doc):
        doc.add_heading('8. CONCLUSION', level=1)
        self._add_para(doc, "The environmental impact of artificial intelligence represents one of the defining challenges of the digital age.")
        doc.add_page_break()

    def _build_references(self, doc):
        doc.add_heading('REFERENCES', level=1)
        refs = [
            "[1] International Energy Agency (IEA). (2025). Energy and AI: Special Report. Paris: IEA Publications.",
            "[2] Patterson, D., Gonzalez, J., Le, Q., et al. (2021). Carbon emissions and large neural network training. arXiv:2104.10350.",
            "[3] de Vries, A. (2023). The growing energy footprint of artificial intelligence. Joule, 7(10), 2191-2194.",
        ]
        for ref in refs:
            p = doc.add_paragraph(ref)
            p.paragraph_format.space_after = Pt(4)
            for run in p.runs:
                run.font.name = self.font_name
                run.font.size = Pt(10)
        doc.add_page_break()

    def _build_appendices(self, doc, data):
        doc.add_heading('APPENDIX A: DATA TABLES', level=1)
        doc.add_heading('APPENDIX B: GLOSSARY OF TERMS', level=1)
