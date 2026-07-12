#!/usr/bin/env python3
"""
AI & Climate Change Research Document Generator
===============================================
A complete pipeline for generating academic research documents
with data visualization, analysis, and professional formatting.

Author: Research Team
Date: 2026-07-10
License: MIT
"""

import argparse
import logging
import sys
from pathlib import Path

from src.data_collection.data_sources import DataCollector
from src.analysis.energy_analysis import EnergyAnalyzer
from src.analysis.carbon_analysis import CarbonAnalyzer
from src.analysis.water_analysis import WaterAnalyzer
from src.visualization.chart_generator import ChartGenerator
from src.document_builder.report_builder import ReportBuilder

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DocumentPipeline:
    """Main pipeline orchestrating the document generation process."""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.collector = DataCollector()
        self.energy_analyzer = EnergyAnalyzer()
        self.carbon_analyzer = CarbonAnalyzer()
        self.water_analyzer = WaterAnalyzer()
        self.chart_gen = ChartGenerator()
        self.report_builder = ReportBuilder()

    def run_data_collection(self) -> dict:
        """Collect all necessary data from various sources."""
        logger.info("Starting data collection phase...")
        data = {
            'datacenter_energy': self.collector.get_datacenter_energy_data(),
            'ai_workload_share': self.collector.get_ai_workload_data(),
            'carbon_intensity': self.collector.get_carbon_intensity_by_region(),
            'water_consumption': self.collector.get_water_consumption_data(),
            'training_costs': self.collector.get_model_training_costs(),
            'mitigation_scores': self.collector.get_mitigation_impact_scores(),
            'jevons_data': self.collector.get_jevons_paradox_data(),
        }
        logger.info("Data collection completed successfully")
        return data

    def run_analysis(self, data: dict) -> dict:
        """Perform analytical computations on collected data."""
        logger.info("Starting analysis phase...")
        results = {
            'energy_projections': self.energy_analyzer.project_future_demand(
                data['datacenter_energy'], data['ai_workload_share']
            ),
            'carbon_footprint': self.carbon_analyzer.calculate_footprint(
                data['datacenter_energy'], data['carbon_intensity']
            ),
            'water_projections': self.water_analyzer.project_demand(
                data['water_consumption']
            ),
            'training_vs_inference': self.energy_analyzer.analyze_training_inference_split(),
        }
        logger.info("Analysis phase completed")
        return results

    def generate_visualizations(self, data: dict, results: dict) -> list:
        """Generate all charts and figures for the document."""
        logger.info("Generating visualizations...")
        figures = []

        figures.append(self.chart_gen.fig1_datacenter_consumption(
            data['datacenter_energy']
        ))
        figures.append(self.chart_gen.fig2_ai_share(
            data['ai_workload_share']
        ))
        figures.append(self.chart_gen.fig3_carbon_intensity(
            data['carbon_intensity']
        ))
        figures.append(self.chart_gen.fig4_training_inference_split(
            results['training_vs_inference']
        ))
        figures.append(self.chart_gen.fig5_water_consumption(
            data['water_consumption']
        ))
        figures.append(self.chart_gen.fig6_carbon_projections(
            results['carbon_footprint']
        ))
        figures.append(self.chart_gen.fig7_mitigation_applications(
            data['mitigation_scores']
        ))
        figures.append(self.chart_gen.fig8_jevons_paradox(
            data['jevons_data']
        ))

        logger.info(f"Generated {len(figures)} figures")
        return figures

    def build_document(self, data: dict, results: dict, figures: list) -> str:
        """Build the final Word document."""
        logger.info("Building final document...")
        output_path = self.report_builder.build(
            data=data,
            results=results,
            figures=figures,
            title="Artificial Intelligence and Its Impact on Environment and Climate Change",
            author="Research Team",
            date="2026-07-10"
        )
        logger.info(f"Document saved to: {output_path}")
        return output_path

    def run(self) -> str:
        """Execute the complete pipeline."""
        logger.info("=" * 60)
        logger.info("AI & Climate Change Document Generator")
        logger.info("=" * 60)

        data = self.run_data_collection()
        results = self.run_analysis(data)
        figures = self.generate_visualizations(data, results)
        output_path = self.build_document(data, results, figures)

        logger.info("=" * 60)
        logger.info("Pipeline completed successfully!")
        logger.info(f"Output: {output_path}")
        logger.info("=" * 60)
        return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate AI & Climate Change Research Document"
    )
    parser.add_argument(
        "--config", "-c",
        default="config.yaml",
        help="Path to configuration file"
    )
    parser.add_argument(
        "--output", "-o",
        default="output",
        help="Output directory"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    pipeline = DocumentPipeline(config_path=args.config)
    output_path = pipeline.run()

    print(f"\n✓ Document generated: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
