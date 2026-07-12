"""
Chart Generator Module
======================
Generates publication-quality figures for academic documents.

All charts are rendered at 300 DPI for print quality and follow
academic formatting conventions with proper labels, legends, and
color schemes.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Patch
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

# Set publication-quality defaults
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16

# Color palette for consistent branding
COLORS = {
    'primary': '#1f4e79',
    'secondary': '#c55a11',
    'accent': '#2e7d32',
    'warning': '#c62828',
    'neutral': '#a5a5a5',
    'low_carbon': '#2e7d32',
    'moderate_carbon': '#f9a825',
    'high_carbon': '#c62828'
}


class ChartGenerator:
    """
    Generates publication-quality charts for research documents.

    Attributes:
        output_dir (Path): Directory for saving generated figures
        fig_count (int): Counter for figure numbering
    """

    def __init__(self, output_dir: str = "figures"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.fig_count = 0
        logger.info("ChartGenerator initialized")

    def _save_fig(self, fig, name: str) -> str:
        """Save figure to output directory."""
        self.fig_count += 1
        filename = f"figure{self.fig_count}_{name}.png"
        filepath = self.output_dir / filename
        fig.savefig(filepath, bbox_inches='tight', dpi=300, 
                   facecolor='white', edgecolor='none')
        plt.close(fig)
        logger.info(f"Saved figure: {filepath}")
        return str(filepath)

    def fig1_datacenter_consumption(self, data: Dict) -> str:
        """
        Figure 1: Global Data Center Electricity Consumption.

        Args:
            data: Dictionary with years, total_dc, ai_specific values

        Returns:
            str: Path to saved figure
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        years = data.get('years', [2022, 2024, 2025, 2026, 2030])
        total_dc = data.get('total_dc', [340, 415, 470, 545, 945])
        ai_specific = data.get('ai_specific', [30, 85, 135, 200, 430])

        x = np.arange(len(years))
        width = 0.35

        bars1 = ax.bar(x - width/2, total_dc, width, 
                       label='Total Data Center', color=COLORS['primary'],
                       edgecolor='black', linewidth=0.5)
        bars2 = ax.bar(x + width/2, ai_specific, width,
                       label='AI-Specific', color=COLORS['secondary'],
                       edgecolor='black', linewidth=0.5)

        ax.set_ylabel('Electricity Consumption (TWh)', fontweight='bold')
        ax.set_xlabel('Year', fontweight='bold')
        ax.set_title('Figure 1: Global Data Center Electricity Consumption (2022–2030)',
                     fontweight='bold', pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(years)
        ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
        ax.set_ylim(0, 1100)
        ax.grid(axis='y', alpha=0.3)

        # Add value labels
        for bar in bars1:
            height = bar.get_height()
            ax.annotate(f'{int(height)}',
                       xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords="offset points",
                       ha='center', va='bottom', fontsize=9)
        for bar in bars2:
            height = bar.get_height()
            ax.annotate(f'{int(height)}',
                       xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords="offset points",
                       ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        return self._save_fig(fig, 'datacenter_consumption')

    def fig2_ai_share(self, data: Dict) -> str:
        """Figure 2: AI Share of Data Center Power."""
        fig, ax = plt.subplots(figsize=(9, 6))

        years = data.get('years', [2022, 2024, 2026, 2030])
        ai_share = data.get('ai_share_pct', [9, 20, 37, 46])
        non_ai_share = data.get('non_ai_share_pct', [91, 80, 63, 54])

        x = np.arange(len(years))
        width = 0.5

        ax.bar(x, ai_share, width, label='AI Workloads', 
               color=COLORS['secondary'], edgecolor='black', linewidth=0.5)
        ax.bar(x, non_ai_share, width, bottom=ai_share,
               label='Non-AI Workloads', color=COLORS['neutral'],
               edgecolor='black', linewidth=0.5)

        for i, (ai, non_ai) in enumerate(zip(ai_share, non_ai_share)):
            ax.annotate(f'{ai}%', xy=(i, ai/2), ha='center', va='center',
                       fontsize=11, fontweight='bold', color='white')
            ax.annotate(f'{non_ai}%', xy=(i, ai + non_ai/2), 
                       ha='center', va='center', fontsize=11, 
                       fontweight='bold', color='white')

        ax.set_ylabel('Share of Data Center Power (%)', fontweight='bold')
        ax.set_xlabel('Year', fontweight='bold')
        ax.set_title('Figure 2: AI Share of Global Data Center Electricity Consumption',
                     fontweight='bold', pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(years)
        ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
        ax.set_ylim(0, 100)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        return self._save_fig(fig, 'ai_share')

    def fig3_carbon_intensity(self, data: Dict) -> str:
        """Figure 3: Grid Carbon Intensity by Region."""
        fig, ax = plt.subplots(figsize=(10, 6))

        regions = data.get('regions', [])
        intensity = data.get('intensity_gco2_kwh', [])

        colors = [COLORS['low_carbon'] if c < 100 
                 else (COLORS['moderate_carbon'] if c < 400 else COLORS['high_carbon'])
                 for c in intensity]

        bars = ax.barh(regions, intensity, color=colors, 
                      edgecolor='black', linewidth=0.5)
        ax.set_xlabel('Carbon Intensity (gCO₂/kWh)', fontweight='bold')
        ax.set_title('Figure 3: Grid Carbon Intensity by Region (2025)',
                     fontweight='bold', pad=15)
        ax.grid(axis='x', alpha=0.3)

        for bar, val in zip(bars, intensity):
            ax.annotate(f'{val}', xy=(val + 15, bar.get_y() + bar.get_height()/2),
                       va='center', fontsize=10, fontweight='bold')

        legend_elements = [
            Patch(facecolor=COLORS['low_carbon'], label='Low (<100 gCO₂/kWh)'),
            Patch(facecolor=COLORS['moderate_carbon'], label='Moderate (100–400 gCO₂/kWh)'),
            Patch(facecolor=COLORS['high_carbon'], label='High (>400 gCO₂/kWh)')
        ]
        ax.legend(handles=legend_elements, loc='lower right', 
                 fontsize=9, frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        return self._save_fig(fig, 'carbon_intensity')

    def fig4_training_inference_split(self, data: Dict) -> str:
        """Figure 4: Training vs Inference Energy Distribution."""
        fig, ax = plt.subplots(figsize=(8, 8))

        labels = ['Inference\n(80–90%)', 'Training\n(10–20%)']
        sizes = [85, 15]
        colors_pie = [COLORS['primary'], COLORS['secondary']]
        explode = (0.05, 0)

        wedges, texts, autotexts = ax.pie(
            sizes, explode=explode, labels=labels, colors=colors_pie,
            autopct='%1.0f%%', shadow=True, startangle=90,
            textprops={'fontsize': 12, 'fontweight': 'bold'},
            wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(14)

        ax.set_title('Figure 4: Distribution of AI Computing Energy\n'
                    '(Training vs. Inference, 2025)',
                    fontweight='bold', pad=20)

        plt.tight_layout()
        return self._save_fig(fig, 'training_inference')

    def fig5_water_consumption(self, data: Dict) -> str:
        """Figure 5: Hyperscaler Water Consumption."""
        fig, ax = plt.subplots(figsize=(10, 6))

        companies = data.get('companies', ['Google', 'Microsoft', 'Meta'])
        water = data.get('water_million_m3', [9.1, 7.8, 3.5])
        yoy = data.get('yoy_change_pct', [17, 22, 15])

        x = np.arange(len(companies))
        width = 0.35

        colors = ['#4285f4', '#00a4ef', '#0668e1']
        bars = ax.bar(x, water, width, color=colors, 
                     edgecolor='black', linewidth=0.5)

        ax.set_ylabel('Water Consumption (Million m³)', fontweight='bold')
        ax.set_xlabel('Company', fontweight='bold')
        ax.set_title('Figure 5: Hyperscaler Water Consumption for Data Center Cooling',
                     fontweight='bold', pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(companies)
        ax.grid(axis='y', alpha=0.3)

        for bar, val, change in zip(bars, water, yoy):
            ax.annotate(f'{val} M m³\n(+{change}% YoY)',
                       xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                       xytext=(0, 5), textcoords="offset points",
                       ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.tight_layout()
        return self._save_fig(fig, 'water_consumption')

    def fig6_carbon_projections(self, data: Dict) -> str:
        """Figure 6: Projected AI-Related CO2 Emissions."""
        fig, ax = plt.subplots(figsize=(10, 6))

        years = ['2021', '2023', '2025', '2027', '2030']
        low_scenario = [0.05, 0.5, 2.5, 8.0, 20.0]
        high_scenario = [0.1, 1.2, 5.0, 15.0, 40.0]

        ax.fill_between(years, low_scenario, high_scenario, 
                       alpha=0.3, color=COLORS['secondary'], 
                       label='Uncertainty Range')
        ax.plot(years, low_scenario, 'o-', color=COLORS['primary'],
               linewidth=2.5, markersize=8, label='Conservative Estimate')
        ax.plot(years, high_scenario, 's-', color=COLORS['warning'],
               linewidth=2.5, markersize=8, label='Aggressive Growth')

        ax.set_ylabel('Annual CO₂ Emissions (MtCO₂)', fontweight='bold')
        ax.set_xlabel('Year', fontweight='bold')
        ax.set_title('Figure 6: Projected AI-Related Annual CO₂ Emissions (2021–2030)',
                     fontweight='bold', pad=15)
        ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 45)

        ax.annotate('Training GPT-4:\n~50 GWh', xy=('2023', 1.2), 
                   xytext=('2021', 3.5),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                   fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

        plt.tight_layout()
        return self._save_fig(fig, 'carbon_projection')

    def fig7_mitigation_applications(self, data: Dict) -> str:
        """Figure 7: AI Applications for Climate Mitigation."""
        fig, ax = plt.subplots(figsize=(10, 6))

        applications = data.get('applications', [])
        scores = data.get('impact_scores', [92, 88, 75, 82, 90, 78, 85, 80])

        colors_bar = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(applications)))

        bars = ax.barh(applications, scores, color=colors_bar,
                      edgecolor='black', linewidth=0.5)
        ax.set_xlabel('Climate Mitigation Impact Score (0–100)', fontweight='bold')
        ax.set_title('Figure 7: AI Applications for Climate Change Mitigation\n'
                    '(Impact Assessment, 2025)',
                    fontweight='bold', pad=15)
        ax.set_xlim(0, 100)
        ax.grid(axis='x', alpha=0.3)

        for bar, score in zip(bars, scores):
            ax.annotate(f'{score}', xy=(score + 1, bar.get_y() + bar.get_height()/2),
                       va='center', fontsize=11, fontweight='bold')

        plt.tight_layout()
        return self._save_fig(fig, 'mitigation_applications')

    def fig8_jevons_paradox(self, data: Dict) -> str:
        """Figure 8: The Jevons Paradox in AI Energy Consumption."""
        fig, ax = plt.subplots(figsize=(10, 6))

        years = data.get('years', ['2020', '2021', '2022', '2023', '2024', '2025', '2026'])
        efficiency = data.get('efficiency_index', [100, 95, 88, 75, 60, 48, 35])
        queries = data.get('total_queries_index', [100, 150, 280, 520, 950, 1800, 3500])

        ax_twin = ax.twinx()

        line1 = ax.plot(years, efficiency, 'o-', color=COLORS['accent'],
                       linewidth=2.5, markersize=8, 
                       label='Energy per Query (Index)')
        line2 = ax_twin.plot(years, queries, 's-', color=COLORS['warning'],
                            linewidth=2.5, markersize=8,
                            label='Total AI Queries (Index)')

        ax.set_ylabel('Energy per Query (Index, 2020=100)', 
                     fontweight='bold', color=COLORS['accent'])
        ax_twin.set_ylabel('Total AI Queries (Index, 2020=100)',
                          fontweight='bold', color=COLORS['warning'])
        ax.set_xlabel('Year', fontweight='bold')
        ax.set_title('Figure 8: The Jevons Paradox in AI Energy Consumption\n'
                    '(Efficiency Gains vs. Total Demand Growth)',
                    fontweight='bold', pad=15)

        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax.legend(lines, labels, loc='center right', 
                 fontsize=10, frameon=True, fancybox=True, shadow=True)

        ax.grid(alpha=0.3)
        ax.set_ylim(0, 120)
        ax_twin.set_ylim(0, 4000)

        plt.tight_layout()
        return self._save_fig(fig, 'jevons_paradox')

    def generate_all_figures(self, data: Dict) -> List[str]:
        """Generate all figures for the document."""
        figures = []
        figures.append(self.fig1_datacenter_consumption(data.get('datacenter_energy', {})))
        figures.append(self.fig2_ai_share(data.get('ai_workload_share', {})))
        figures.append(self.fig3_carbon_intensity(data.get('carbon_intensity', {})))
        figures.append(self.fig4_training_inference_split(data.get('training_inference', {})))
        figures.append(self.fig5_water_consumption(data.get('water_consumption', {})))
        figures.append(self.fig6_carbon_projections(data.get('carbon_projections', {})))
        figures.append(self.fig7_mitigation_applications(data.get('mitigation_scores', {})))
        figures.append(self.fig8_jevons_paradox(data.get('jevons_data', {})))
        return figures


class ChartStyle:
    """Custom chart styling utilities."""

    @staticmethod
    def apply_academic_style(ax):
        """Apply academic formatting to an axis."""
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='both', which='major', labelsize=10)
        ax.grid(alpha=0.3, linestyle='--')

    @staticmethod
    def add_source_note(ax, text: str, fontsize: int = 8):
        """Add source note to bottom of figure."""
        ax.text(0.5, -0.15, f"Source: {text}", 
               transform=ax.transAxes, ha='center', va='top',
               fontsize=fontsize, style='italic')

    @staticmethod
    def format_axis_labels(ax, xlabel: str = None, ylabel: str = None, 
                          title: str = None):
        """Format axis labels with consistent styling."""
        if xlabel:
            ax.set_xlabel(xlabel, fontweight='bold', fontsize=12)
        if ylabel:
            ax.set_ylabel(ylabel, fontweight='bold', fontsize=12)
        if title:
            ax.set_title(title, fontweight='bold', fontsize=14, pad=15)
