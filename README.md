<div align="center">

# Hi, I'm Alex Huang 👋

### Quant Research × Rust Systems × High-Performance Data Infrastructure

I build tools for **alpha research**, **backtesting**, **model inference**, and **developer productivity** — with a strong preference for Rust, Polars, Python, and clean system boundaries.

[![GitHub followers](https://img.shields.io/github/followers/huangbogeng?style=social)](https://github.com/huangbogeng)
[![Profile views](https://komarev.com/ghpvc/?username=huangbogeng\&style=flat-square)](https://github.com/huangbogeng)
[![Rust](https://img.shields.io/badge/Rust-systems%20%26%20performance-orange?logo=rust)](https://www.rust-lang.org/)
[![Python](https://img.shields.io/badge/Python-quant%20research-blue?logo=python)](https://www.python.org/)
[![Polars](https://img.shields.io/badge/Polars-dataframe%20engine-cyan)](https://pola.rs/)

</div>

---

## What I focus on

I care about building research infrastructure that is **fast, explicit, testable, and close to production**.

* ⚡ **Performance engineering**: Rust-native libraries, low-latency data paths, CPU inference, and async/non-blocking designs.
* 📈 **Quant research tooling**: factor mining, backtesting engines, trading calendars, data access layers, and analysis workflows.
* 🧠 **ML infrastructure**: lightweight model runtimes and predictable inference behavior.
* 🛠️ **Developer tools**: small utilities that remove friction from daily engineering workflows.

---

## Featured projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/huangbogeng/nanolog-rs">nanolog-rs</a></h3>
      <p><strong>High-performance non-blocking logging for Rust.</strong></p>
      <p>Built around a Disruptor-style ring buffer, batch flushing, preallocated records, thread-safe counters, and graceful shutdown semantics.</p>
      <p>
        <img src="https://img.shields.io/badge/Rust-logging-orange?logo=rust" />
        <img src="https://img.shields.io/badge/focus-low_latency-blue" />
        <img src="https://img.shields.io/badge/license-MIT-green" />
      </p>
      <p><a href="https://crates.io/crates/nanolog-rs"><img src="https://img.shields.io/crates/v/nanolog-rs.svg" /></a></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/huangbogeng/polars_bt_extension">polars_bt_extension</a></h3>
      <p><strong>A Rust-powered backtesting plugin for Polars.</strong></p>
      <p>Designed for strategy evaluation with efficient order matching, long/short position tracking, limit price handling, and a Python API that integrates with Polars DataFrames.</p>
      <p>
        <img src="https://img.shields.io/badge/Rust-Polars_plugin-orange?logo=rust" />
        <img src="https://img.shields.io/badge/Python-API-blue?logo=python" />
        <img src="https://img.shields.io/badge/domain-backtesting-purple" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/GDUF-QUANTLAB/alpha-lab">alpha-lab</a></h3>
      <p><strong>A high-performance alpha mining framework.</strong></p>
      <p>Provides an integrated research workflow for factor researchers: trading calendars, data access, factor construction, Rack-based data integration, and Polens factor analysis.</p>
      <p>
        <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python" />
        <img src="https://img.shields.io/badge/Polars-fast-cyan" />
        <img src="https://img.shields.io/badge/domain-alpha_research-green" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/huangbogeng/xgboost-rs">xgboost-rs</a></h3>
      <p><strong>A focused Rust inference runtime for official XGBoost <code>model.json</code> files.</strong></p>
      <p>Loads supported upstream models, runs CPU prediction, validates model boundaries, and fails explicitly when a model is outside the supported scope.</p>
      <p>
        <img src="https://img.shields.io/badge/Rust-ML_inference-orange?logo=rust" />
        <img src="https://img.shields.io/badge/XGBoost-model.json-red" />
        <img src="https://img.shields.io/badge/focus-correctness-blue" />
      </p>
      <p>
        <a href="https://crates.io/crates/xgboost-rs"><img src="https://img.shields.io/crates/v/xgboost-rs.svg" /></a>
        <a href="https://docs.rs/xgboost-rs"><img src="https://docs.rs/xgboost-rs/badge.svg" /></a>
      </p>
    </td>
  </tr>
</table>

### Developer tool highlight

<table>
  <tr>
    <td valign="top">
      <h3><a href="https://github.com/huangbogeng/cc-switch-ui">cc-switch-ui</a></h3>
      <p><strong>A browser-based management UI for Claude Code provider configurations.</strong></p>
      <p>Replaces manual JSON editing with one-click provider switching, built-in provider presets, API key / OAuth flows, local proxy support, and live synchronization with Claude Code configuration.</p>
      <p>
        <img src="https://img.shields.io/badge/Rust-Axum-orange?logo=rust" />
        <img src="https://img.shields.io/badge/React-TypeScript-blue?logo=react" />
        <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey" />
      </p>
    </td>
  </tr>
</table>

---

## Open Source Contributions

- **[abstractqqq/polars_ds_extension #477](https://github.com/abstractqqq/polars_ds_extension/pull/477)**  
  Added finite-window exponentially weighted rolling linear regression.

- **[Point72/polars-io-tools #50](https://github.com/Point72/polars-io-tools/pull/50)**  
  Fixed ClickHouse HTTP response decompression.

- **Aequiludium ecosystem**  
  Ongoing contributions across research infrastructure, trading calendars, data pipelines, factor analysis, backtesting, and portfolio optimization.

---

## Tech stack

<p>
  <img src="https://skillicons.dev/icons?i=rust,python,ts,react,vite,linux,git,github,docker" />
</p>

**Core interests:** Rust, Python, Polars, PyO3, Maturin, Axum, React, TypeScript, quantitative research systems, backtesting engines, factor analysis, model inference.

---

## Project map

| Area                    | Project                                                                   | What it demonstrates                                                     |
| ----------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Logging infrastructure  | [nanolog-rs](https://github.com/huangbogeng/nanolog-rs)                   | Non-blocking Rust logging, ring buffers, batching, graceful shutdown     |
| Backtesting engine      | [polars_bt_extension](https://github.com/huangbogeng/polars_bt_extension) | Rust + Polars plugin design, order matching, P&L calculation             |
| Alpha research platform | [alpha-lab](https://github.com/GDUF-QUANTLAB/alpha-lab)                   | Factor research workflow, data access, trading calendars, analysis tools |
| ML inference runtime    | [xgboost-rs](https://github.com/huangbogeng/xgboost-rs)                   | Rust-native XGBoost model loading and CPU prediction                     |
| Developer productivity  | [cc-switch-ui](https://github.com/huangbogeng/cc-switch-ui)               | Rust backend + React frontend + local config automation                  |

---

## GitHub stats

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=huangbogeng&show_icons=true&theme=transparent&hide_border=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=huangbogeng&layout=compact&theme=transparent&hide_border=true" />
</div>

---

## Working style

> Make the research loop faster.
> Make the system boundary clearer.
> Make correctness visible before performance becomes dangerous.

I like projects that sit at the intersection of **research productivity** and **systems engineering**: small enough to understand, fast enough to matter, and explicit enough to trust.

---

<div align="center">

### Thanks for visiting.

If you are interested in quant infrastructure, Rust performance engineering, or research tooling, feel free to explore the repositories above.

</div>
