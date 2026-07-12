# AI & Climate Change Research Document Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> A comprehensive Python pipeline for generating publication-quality academic research documents on the environmental impact of artificial intelligence, complete with data visualization, statistical analysis, and professional Word document formatting.

## Features

- **Data Collection**: Structured data from IEA reports, corporate sustainability disclosures, and academic literature
- **Statistical Analysis**: Energy projection models, carbon footprint calculations, water demand forecasting
- **Publication-Quality Visualizations**: 8 professional charts at 300 DPI with academic color schemes
- **Automated Document Generation**: Complete Word documents with tables of contents, figures, tables, and 110+ references
- **Modular Architecture**: Clean separation of concerns across data, analysis, visualization, and document building

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-climate-research.git
cd ai-climate-research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Generate the complete document
python main.py

# With custom configuration
python main.py --config config.yaml --output ./my_output

# Verbose mode for debugging
python main.py --verbose
```

### Jupyter Notebook

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

## Project Structure

```
ai-climate-research/
├── main.py                      # Entry point
├── config.yaml                  # Configuration
├── requirements.txt             # Dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── src/
│   ├── data_collection/         # Data ingestion
│   │   ├── __init__.py
│   │   └── data_sources.py
│   ├── analysis/                # Statistical analysis
│   │   ├── __init__.py
│   │   └── energy_analysis.py
│   ├── visualization/           # Chart generation
│   │   ├── __init__.py
│   │   └── chart_generator.py
│   └── document_builder/        # Word document builder
│       ├── __init__.py
│       └── report_builder.py
│
├── data/
│   ├── raw/                     # Raw data files
│   ├── processed/                 # Processed datasets
│   └── cache/                   # Cached API responses
│
├── figures/                     # Generated visualizations
├── output/                      # Final documents
├── notebooks/                   # Jupyter notebooks
├── tests/                       # Unit tests
└── docs/                        # Documentation
```

## Generated Document Contents

The pipeline generates a comprehensive academic document including:

### Chapters
1. **Introduction** - Background, scope, and methodology
2. **Environmental Footprint** - Energy, water, carbon, e-waste, rare earth minerals
3. **AI in Climate Mitigation** - Renewable energy, smart grid, CCS, agriculture, modeling, transportation
4. **Jevons Paradox** - Efficiency gains vs. demand growth, case studies
5. **Regulatory Frameworks** - EU, US, China, international standards
6. **Sustainable AI** - Green data centers, carbon-aware computing, model efficiency, hardware innovation, circular economy
7. **Future Outlook** - Projected trends, research priorities, policy recommendations
8. **Conclusion** - Synthesis and call to action

### Visualizations
- Figure 1: Global Data Center Electricity Consumption (2022-2030)
- Figure 2: AI Share of Global Data Center Power
- Figure 3: Grid Carbon Intensity by Region
- Figure 4: Training vs Inference Energy Distribution
- Figure 5: Hyperscaler Water Consumption
- Figure 6: Projected AI-Related CO2 Emissions
- Figure 7: AI Applications for Climate Mitigation
- Figure 8: The Jevons Paradox in AI

### Tables
- Table 1: AI Model Training Energy & Emissions
- Table 2: Per-Task Energy Consumption
- Table 3: Hyperscaler Water Consumption
- Table 4: Carbon Emissions by Grid Scenario
- Table 5: Critical Minerals in AI Hardware
- Table 6: EU Regulatory Instruments
- Table 7: Data Center Efficiency Metrics

### References
- 110 peer-reviewed citations, government reports, and industry disclosures

## Data Sources

- International Energy Agency (IEA) Energy and AI Report (2025)
- Google, Microsoft, Meta, Amazon Sustainability Reports (2024-2025)
- USGS Mineral Commodity Summaries (2025)
- Ember Global Electricity Review (2025)
- Academic literature from Nature, Joule, Science, and arXiv

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Specific test module
pytest tests/test_energy_analysis.py
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## Citation

If you use this code in your research, please cite:

```bibtex
@software{ai_climate_research_2026,
  title={AI and Climate Change Research Document Generator},
  author={Research Team},
  year={2026},
  url={https://github.com/yourusername/ai-climate-research}
}
```

## Acknowledgments

- International Energy Agency for energy data
- Google DeepMind for AI forecasting research
- The Shift Project for digital sobriety framework
- All researchers cited in the reference list
