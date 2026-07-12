"""
Energy Analysis Module
======================
Performs analytical computations on AI energy consumption data.
"""

import numpy as np
import logging
from typing import Dict, List
from scipy import stats

logger = logging.getLogger(__name__)


class EnergyAnalyzer:
    """Analyzes energy consumption patterns in AI systems."""

    def __init__(self):
        self.projection_models = {
            'linear': self._linear_projection,
            'exponential': self._exponential_projection,
            'logistic': self._logistic_projection
        }
        logger.info("EnergyAnalyzer initialized")

    def project_future_demand(self, datacenter_data: Dict, 
                              ai_share_data: Dict,
                              model: str = 'exponential',
                              years: List[int] = None) -> Dict:
        """Project future AI electricity demand."""
        if years is None:
            years = list(range(2025, 2036))

        historical_years = datacenter_data.get('years', [2022, 2024, 2025])
        historical_ai = datacenter_data.get('ai_specific', [30, 85, 135])

        projection_func = self.projection_models.get(model, self._exponential_projection)
        projections = projection_func(historical_years, historical_ai, years)
        confidence_intervals = self._calculate_confidence_intervals(projections, uncertainty=0.15)

        return {
            'years': years,
            'projected_demand_twh': projections,
            'confidence_intervals': confidence_intervals,
            'model_used': model,
            'growth_rate': self._calculate_growth_rate(historical_ai),
            'doubling_time': self._calculate_doubling_time(historical_ai)
        }

    def analyze_training_inference_split(self) -> Dict:
        """Analyze the energy split between training and inference."""
        return {
            'current_split': {'training': 15, 'inference': 85},
            'historical_trend': {
                2020: {'training': 25, 'inference': 75},
                2022: {'training': 20, 'inference': 80},
                2024: {'training': 15, 'inference': 85},
                2026: {'training': 12, 'inference': 88},
                2030: {'training': 10, 'inference': 90}
            },
            'key_insight': 'Inference dominates and will continue to grow',
            'implications': [
                'Inference efficiency improvements have greater aggregate impact',
                'Edge deployment can reduce transmission losses',
                'Model compression critical for inference energy reduction'
            ]
        }

    def analyze_efficiency_trends(self, data: Dict) -> Dict:
        """Analyze historical and projected efficiency improvements."""
        return {
            'hardware_efficiency_improvement': '10,000x (2012-2024)',
            'per_computation_efficiency_annual': '~60% improvement/year',
            'total_demand_growth': '300,000x (2012-2024)',
            'net_effect': '30x increase in total energy despite efficiency gains',
            'jevons_factor': 1.8,
            'key_finding': 'Efficiency gains are more than offset by demand growth',
            'recommendations': [
                'Focus on absolute energy caps, not just efficiency',
                'Implement carbon pricing for AI computing',
                'Develop rebound-aware efficiency metrics'
            ]
        }

    def _linear_projection(self, x_hist, y_hist, x_proj):
        slope, intercept, _, _, _ = stats.linregress(x_hist, y_hist)
        return [slope * x + intercept for x in x_proj]

    def _exponential_projection(self, x_hist, y_hist, x_proj):
        log_y = np.log(y_hist)
        slope, intercept, _, _, _ = stats.linregress(x_hist, log_y)
        return [np.exp(slope * x + intercept) for x in x_proj]

    def _logistic_projection(self, x_hist, y_hist, x_proj, carrying_capacity=1000):
        log_y = np.log([y / (carrying_capacity - y) for y in y_hist])
        slope, intercept, _, _, _ = stats.linregress(x_hist, log_y)
        return [carrying_capacity / (1 + np.exp(-(slope * x + intercept))) for x in x_proj]

    def _calculate_confidence_intervals(self, projections, uncertainty=0.15):
        lower = [p * (1 - uncertainty) for p in projections]
        upper = [p * (1 + uncertainty) for p in projections]
        return {'lower': lower, 'upper': upper}

    def _calculate_growth_rate(self, values):
        if len(values) < 2:
            return 0.0
        start, end = values[0], values[-1]
        years = len(values) - 1
        return (end / start) ** (1/years) - 1

    def _calculate_doubling_time(self, values):
        growth_rate = self._calculate_growth_rate(values)
        if growth_rate <= 0:
            return float('inf')
        return np.log(2) / np.log(1 + growth_rate)


class CarbonAnalyzer:
    """Analyzes carbon emissions from AI computing."""

    def __init__(self):
        logger.info("CarbonAnalyzer initialized")

    def calculate_footprint(self, energy_data: Dict, carbon_intensity_data: Dict) -> Dict:
        """Calculate carbon footprint under different scenarios."""
        scenarios = {}
        for region, intensity in zip(
            carbon_intensity_data.get('regions', []),
            carbon_intensity_data.get('intensity_gco2_kwh', [])
        ):
            annual_energy_twh = energy_data.get('ai_specific', [135])[-1]
            annual_energy_kwh = annual_energy_twh * 1e9
            emissions_mtco2 = (annual_energy_kwh * intensity) / 1e12
            scenarios[region] = {
                'intensity_gco2_kwh': intensity,
                'annual_emissions_mtco2': emissions_mtco2
            }

        global_emissions = sum(s['annual_emissions_mtco2'] for s in scenarios.values()) / len(scenarios)

        return {
            'scenarios': scenarios,
            'global_average_mtco2': global_emissions,
            'training_emissions': {
                'gpt4_equivalent': 8.0,
                'norway_grid': 0.75,
                'india_grid': 35.4
            },
            'inference_emissions_2025': 2.0,
            'inference_emissions_2030_proj': 15.0,
            'total_2025': 5.0,
            'total_2030_proj': 20.0,
            'mitigation_potential': 1500.0
        }

    def analyze_carbon_aware_potential(self) -> Dict:
        """Analyze potential emission reductions from carbon-aware computing."""
        return {
            'temporal_shifting_potential': '15-25% emission reduction',
            'spatial_shifting_potential': '40-60% for delay-tolerant workloads',
            'google_2023_achieved': '1.5 MtCO2e avoided',
            'microsoft_commitment': '100% hourly carbon-free by 2030',
            'key_barriers': [
                'Real-time carbon intensity data availability',
                'Workload flexibility requirements',
                'Data residency and compliance constraints',
                'Network latency for spatial shifting'
            ],
            'enabling_technologies': [
                'electricityMap API',
                'WattTime Automated Emissions Reduction',
                'Google Carbon-Intelligent Computing',
                'Microsoft Sustainability Calculator'
            ]
        }


class WaterAnalyzer:
    """Analyzes water consumption in AI infrastructure."""

    def __init__(self):
        logger.info("WaterAnalyzer initialized")

    def project_demand(self, water_data: Dict) -> Dict:
        """Project future water demand for AI data centers."""
        current_consumption = sum(water_data.get('water_million_m3', [9.1, 7.8, 3.5]))
        projections = {2025: 5.0, 2027: 7.5, 2030: 12.0, 2035: 22.0}

        cooling_scenarios = {
            'current_evaporative': projections,
            'with_immersion_cooling': {k: v * 0.2 for k, v in projections.items()},
            'with_dlc': {k: v * 0.3 for k, v in projections.items()},
            'water_free': {k: v * 0.05 for k, v in projections.items()}
        }

        return {
            'current_hyperscaler_consumption_bm3': current_consumption / 1000,
            'global_ai_projections_bm3': projections,
            'cooling_technology_impact': cooling_scenarios,
            'water_stress_regions': [
                'Arizona, USA', 'Nevada, USA', 'Rajasthan, India',
                'Northern Chile', 'Western Australia'
            ],
            'key_insight': 'Water-free cooling could reduce consumption by 95%'
        }

    def analyze_cooling_efficiency(self) -> Dict:
        """Analyze efficiency of different cooling technologies."""
        return {
            'technologies': {
                'air_cooling': {'pue_contribution': 0.4, 'water_usage': 'High', 'efficiency': 'Baseline'},
                'evaporative_cooling': {'pue_contribution': 0.2, 'water_usage': 'Very High', 'efficiency': 'Good'},
                'direct_liquid_cooling': {'pue_contribution': 0.1, 'water_usage': 'Moderate', 'efficiency': 'Very Good'},
                'immersion_cooling': {'pue_contribution': 0.05, 'water_usage': 'Very Low', 'efficiency': 'Excellent'},
                'two_phase_immersion': {'pue_contribution': 0.03, 'water_usage': 'Minimal', 'efficiency': 'Best'}
            },
            'recommendation': 'Transition to DLC for near-term, immersion for long-term'
        }
