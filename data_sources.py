"""
Data Sources Module
===================
Handles collection and preprocessing of environmental data for AI research.

Supports multiple data sources:
- IEA (International Energy Agency)
- Corporate sustainability reports
- Academic literature
- Government databases
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np

logger = logging.getLogger(__name__)


class DataCollector:
    """
    Collects and preprocesses data from various sources for analysis.

    Attributes:
        cache_dir (Path): Directory for caching downloaded data
        sources (dict): Registered data sources
    """

    def __init__(self, cache_dir: str = "data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.sources = {}
        logger.info("DataCollector initialized")

    def get_datacenter_energy_data(self) -> Dict:
        """
        Retrieve global data center electricity consumption data.

        Returns:
            dict: Annual consumption in TWh by year and category
        """
        data = {
            'years': [2022, 2024, 2025, 2026, 2030],
            'total_dc': [340, 415, 470, 545, 945],
            'ai_specific': [30, 85, 135, 200, 430],
            'non_ai': [310, 330, 335, 345, 515],
            'sources': ['IEA Energy and AI Report (2025)', 'Goldman Sachs Research'],
            'notes': '2026 and 2030 values are projections'
        }
        logger.debug("Retrieved datacenter energy data")
        return data

    def get_ai_workload_data(self) -> Dict:
        """
        Get AI share of data center power over time.

        Returns:
            dict: AI workload percentage by year
        """
        data = {
            'years': [2022, 2024, 2026, 2030],
            'ai_share_pct': [9, 20, 37, 46],
            'non_ai_share_pct': [91, 80, 63, 54],
            'source': 'IEA Energy and AI Report (2025)'
        }
        return data

    def get_carbon_intensity_by_region(self) -> Dict:
        """
        Retrieve grid carbon intensity data by region.

        Returns:
            dict: Carbon intensity in gCO2/kWh by country/region
        """
        data = {
            'regions': [
                'Norway', 'France', 'Sweden', 'Canada', 'UK',
                'Germany', 'USA\n(Avg)', 'China', 'India', 'South Africa'
            ],
            'intensity_gco2_kwh': [15, 40, 25, 120, 200, 380, 500, 550, 708, 900],
            'categories': {
                'low': ['Norway', 'France', 'Sweden'],
                'moderate': ['Canada', 'UK', 'Germany'],
                'high': ['USA', 'China', 'India', 'South Africa']
            },
            'source': 'Ember Global Electricity Review (2025)',
            'year': 2025
        }
        return data

    def get_water_consumption_data(self) -> Dict:
        """
        Get hyperscaler water consumption data.

        Returns:
            dict: Water consumption in million cubic meters
        """
        data = {
            'companies': ['Google\n(2024)', 'Microsoft\n(FY24)', 'Meta\n(2024)'],
            'water_million_m3': [9.1, 7.8, 3.5],
            'yoy_change_pct': [17, 22, 15],
            'global_ai_projection_2027': [4.2, 6.6],
            'sources': [
                'Google Environmental Report (2025)',
                'Microsoft Sustainability Report (2025)',
                'Meta Sustainability Report (2025)'
            ]
        }
        return data

    def get_model_training_costs(self) -> Dict:
        """
        Get training energy and emissions for representative AI models.

        Returns:
            dict: Model specifications and environmental costs
        """
        data = {
            'models': [
                {
                    'name': 'GPT-3',
                    'parameters': '175B',
                    'training_energy_mwh': 1287,
                    'co2_tco2e': 552,
                    'year': 2020,
                    'source': 'Patterson et al. (2021)'
                },
                {
                    'name': 'GPT-4',
                    'parameters': 'Est. 1.8T',
                    'training_energy_mwh': 50000,
                    'co2_tco2e': 8000,
                    'year': 2023,
                    'source': 'de Vries (2023)'
                },
                {
                    'name': 'LLaMA 3.1 405B',
                    'parameters': '405B',
                    'training_energy_mwh': 30000,
                    'co2_tco2e': 5500,
                    'year': 2024,
                    'source': 'Meta AI (2024)'
                },
                {
                    'name': 'Gemini Ultra',
                    'parameters': 'Est. 1.5T',
                    'training_energy_mwh': 45000,
                    'co2_tco2e': 7200,
                    'year': 2024,
                    'source': 'Google DeepMind (2024)'
                },
                {
                    'name': 'Claude 3 Opus',
                    'parameters': 'Est. 500B',
                    'training_energy_mwh': 20000,
                    'co2_tco2e': 3500,
                    'year': 2024,
                    'source': 'Anthropic (2024)'
                },
                {
                    'name': 'Mistral Large 2',
                    'parameters': 'Est. 120B',
                    'training_energy_mwh': 5000,
                    'co2_tco2e': 900,
                    'year': 2024,
                    'source': 'Mistral AI LCA (2025)'
                }
            ],
            'assumptions': {
                'grid_carbon_intensity': '400 gCO2/kWh (US average)',
                'note': 'Estimates vary by methodology'
            }
        }
        return data

    def get_mitigation_impact_scores(self) -> Dict:
        """
        Get AI application impact scores for climate mitigation.

        Returns:
            dict: Application names and impact scores (0-100)
        """
        data = {
            'applications': [
                'Renewable Energy\nForecasting',
                'Smart Grid\nOptimization',
                'Carbon Capture\n& Storage',
                'Precision\nAgriculture',
                'Climate Modeling\n& Prediction',
                'Building Energy\nManagement',
                'Transportation\nOptimization',
                'Deforestation\nMonitoring'
            ],
            'impact_scores': [92, 88, 75, 82, 90, 78, 85, 80],
            'criteria': 'Based on emission reduction potential, scalability, and technology readiness',
            'year': 2025
        }
        return data

    def get_jevons_paradox_data(self) -> Dict:
        """
        Get data illustrating the Jevons Paradox in AI.

        Returns:
            dict: Efficiency trends and demand growth over time
        """
        data = {
            'years': ['2020', '2021', '2022', '2023', '2024', '2025', '2026'],
            'efficiency_index': [100, 95, 88, 75, 60, 48, 35],
            'total_queries_index': [100, 150, 280, 520, 950, 1800, 3500],
            'efficiency_label': 'Energy per Query (Index, 2020=100)',
            'demand_label': 'Total AI Queries (Index, 2020=100)',
            'source': 'Compiled from industry reports and academic estimates'
        }
        return data

    def get_inference_energy_data(self) -> Dict:
        """
        Get per-task energy consumption for AI inference.

        Returns:
            dict: Energy and CO2 per task by modality
        """
        data = {
            'tasks': [
                {
                    'type': 'Text Generation (LLaMA 3.1 8B)',
                    'scale': 'Small',
                    'energy': '~0.03 Wh',
                    'co2': '~0.01 gCO2e'
                },
                {
                    'type': 'Text Generation (LLaMA 3.1 405B)',
                    'scale': 'Large',
                    'energy': '~1.9 Wh',
                    'co2': '~0.6 gCO2e'
                },
                {
                    'type': 'Image Generation (Stable Diffusion)',
                    'scale': 'Medium',
                    'energy': '~0.6 Wh',
                    'co2': '~0.2 gCO2e'
                },
                {
                    'type': 'Video Generation (5-sec clip)',
                    'scale': 'Large',
                    'energy': '~0.9 kWh',
                    'co2': '~0.3 kgCO2e'
                },
                {
                    'type': 'Voice Synthesis (1 min)',
                    'scale': 'Medium',
                    'energy': '~0.15 Wh',
                    'co2': '~0.05 gCO2e'
                }
            ],
            'assumptions': 'US average grid carbon intensity (~400 gCO2/kWh)'
        }
        return data

    def get_critical_minerals_data(self) -> Dict:
        """
        Get critical minerals data for AI hardware.

        Returns:
            dict: Mineral applications, sources, and environmental concerns
        """
        data = {
            'minerals': [
                {
                    'name': 'Cobalt',
                    'application': 'Batteries, semiconductors',
                    'primary_source': 'DRC (70%)',
                    'concern': 'Child labor, water pollution'
                },
                {
                    'name': 'Gallium',
                    'application': 'Compound semiconductors',
                    'primary_source': 'China (98%)',
                    'concern': 'Toxic byproduct processing'
                },
                {
                    'name': 'Indium',
                    'application': 'Transparent conductors, displays',
                    'primary_source': 'China, Korea',
                    'concern': 'Acid mine drainage'
                },
                {
                    'name': 'Neodymium',
                    'application': 'Permanent magnets',
                    'primary_source': 'China (60%)',
                    'concern': 'Radioactive tailings'
                },
                {
                    'name': 'Silicon (High-Purity)',
                    'application': 'Semiconductor wafers',
                    'primary_source': 'China, US, Norway',
                    'concern': 'Energy-intensive purification'
                },
                {
                    'name': 'Copper',
                    'application': 'Interconnects, power delivery',
                    'primary_source': 'Chile, Peru, China',
                    'concern': 'Acid rock drainage, habitat loss'
                }
            ],
            'sources': [
                'USGS Mineral Commodity Summaries (2025)',
                'IEA Critical Minerals Market Review (2025)'
            ]
        }
        return data

    def get_regulatory_data(self) -> Dict:
        """
        Get regulatory framework data by jurisdiction.

        Returns:
            dict: Regulations, scope, requirements, and status
        """
        data = {
            'eu_regulations': [
                {
                    'name': 'EU AI Act',
                    'scope': 'High-risk AI systems',
                    'requirements': 'Risk assessment, transparency',
                    'status': 'In force (2025)'
                },
                {
                    'name': 'Energy Efficiency Directive',
                    'scope': 'Data centers >500 kW',
                    'requirements': 'Energy/water reporting',
                    'status': 'In force (2023)'
                },
                {
                    'name': 'ESRS Standards',
                    'scope': 'Large companies',
                    'requirements': 'Scope 1/2/3 disclosure',
                    'status': 'In force (2024)'
                },
                {
                    'name': 'Data Center Regulation (Prop.)',
                    'scope': 'All data centers',
                    'requirements': 'PUE standards, heat recovery',
                    'status': 'Under development'
                },
                {
                    'name': 'CBAM',
                    'scope': 'Import of carbon-intensive goods',
                    'requirements': 'Carbon border tariffs',
                    'status': 'Phased in (2026)'
                }
            ],
            'us_policies': [
                'Better Buildings Initiative (DOE)',
                'Energy Act of 2020',
                'Executive Order on AI (2023)',
                'NIST AI Risk Management Framework',
                'Inflation Reduction Act (2022)'
            ],
            'china_policies': [
                'NDRC Data Center Guidelines (2021)',
                'East Data West Computing Initiative (2022)',
                'Carbon Neutrality Target (2060)',
                'National ETS'
            ]
        }
        return data

    def get_datacenter_efficiency_data(self) -> Dict:
        """
        Get data center efficiency metrics by operator.

        Returns:
            dict: PUE, renewable energy, water efficiency by company
        """
        data = {
            'operators': ['Google', 'Microsoft', 'Amazon AWS', 'Meta', 'Industry Average'],
            'pue': [1.10, 1.12, 1.13, 1.09, 1.55],
            'renewable_pct': ['100%', '100%', '90%', '100%', '35%'],
            'water_efficiency_l_kwh': [0.15, 0.18, 0.20, 0.14, 0.45],
            'waste_heat_recovery': ['Limited pilots', 'Denmark, Finland', 'Limited', 'Denmark, Ireland', '<5%'],
            'sources': [
                'Corporate sustainability reports (2024)',
                'Uptime Institute Global Data Center Survey (2024)'
            ]
        }
        return data

    def get_carbon_scenario_data(self) -> Dict:
        """
        Get carbon emissions under different grid scenarios.

        Returns:
            dict: Emissions by model and grid carbon intensity
        """
        data = {
            'models': [
                'GPT-3 (1,287 MWh)',
                'GPT-4 (50,000 MWh)',
                'LLaMA 3.1 405B (30,000 MWh)',
                'Annual Inference (Global, 2025)',
                'Annual Inference (Global, 2030 Proj.)'
            ],
            'norway_15': ['19 tCO2e', '750 tCO2e', '450 tCO2e', '~75,000 tCO2e', '~300,000 tCO2e'],
            'france_40': ['51 tCO2e', '2,000 tCO2e', '1,200 tCO2e', '~200,000 tCO2e', '~800,000 tCO2e'],
            'us_400': ['515 tCO2e', '20,000 tCO2e', '12,000 tCO2e', '~2,000,000 tCO2e', '~8,000,000 tCO2e'],
            'assumptions': [
                'Inference estimates assume 75 TWh annual AI computing in 2025',
                '300 TWh projected for 2030',
                'Actual emissions depend on workload distribution'
            ]
        }
        return data

    def save_to_cache(self, data: Dict, filename: str):
        """Save collected data to cache directory."""
        filepath = self.cache_dir / filename
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        logger.info(f"Data cached to {filepath}")

    def load_from_cache(self, filename: str) -> Dict:
        """Load data from cache directory."""
        filepath = self.cache_dir / filename
        if filepath.exists():
            with open(filepath, 'r') as f:
                data = json.load(f)
            logger.info(f"Data loaded from cache: {filepath}")
            return data
        else:
            logger.warning(f"Cache file not found: {filepath}")
            return {}


class DataValidator:
    """Validates data integrity and consistency."""

    @staticmethod
    def validate_energy_data(data: Dict) -> bool:
        """Validate energy consumption data."""
        required_keys = ['years', 'total_dc', 'ai_specific']
        return all(k in data for k in required_keys)

    @staticmethod
    def validate_carbon_data(data: Dict) -> bool:
        """Validate carbon intensity data."""
        required_keys = ['regions', 'intensity_gco2_kwh']
        return all(k in data for k in required_keys)

    @staticmethod
    def validate_water_data(data: Dict) -> bool:
        """Validate water consumption data."""
        required_keys = ['companies', 'water_million_m3']
        return all(k in data for k in required_keys)
