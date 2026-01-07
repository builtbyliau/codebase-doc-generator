# Next.js

Next.js is the open-source React framework created by [Vercel](https://vercel.com) that enables developers to build high-performance web applications with features like Server Side Rendering (SSR), Static Site Generation (SSG), and incremental static regeneration.

## Description

Next.js provides a comprehensive solution for building production-ready React applications. It abstracts away the complex configuration required for modern JavaScript tooling, offering an optimized "zero-config" experience while remaining highly extensible. By combining the best of React with an integrated routing system and optimized build pipeline (including the Rust-based **Turbopack**), Next.js allows teams to focus on building products rather than infrastructure.

This repository is a monorepo containing the core framework, internal plugins, benchmarking tools, and the next-generation bundling engine.

## Features

-   **App Router:** Support for Shared Layouts, Nested Routing, Loading States, and Error Handling.
-   **React Server Components (RSC):** Build components that run on the server for reduced bundle sizes and improved performance.
-   **Turbopack:** An incremental bundler optimized for JavaScript and TypeScript, written in Rust, integrated directly into the development workflow.
-   **Data Fetching:** Simplified data fetching with `fetch` extensions, including caching and revalidation at the component level.
-   **Built-in Optimizations:** Automatic Image, Font, and Script optimizations to improve Core Web Vitals.
-   **CSS Support:** Built-in support for CSS Modules, Tailwind CSS, and CSS-in-JS.
-   **Middleware:** Run code before a request is completed for authentication, redirects, or experimentation.
-   **API Routes:** Easily build API endpoints as part of your application.

## Installation

To contribute to the development of Next.js or test the framework from source, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vercel/next.js.git
    cd next.js
    ```

2.  **Install dependencies:**
    The project uses a monorepo structure managed by `pnpm` (referenced in configuration) and `lerna`.
    ```bash
    pnpm install
    ```

3.  **Build the project:**
    ```bash
    pnpm run build
    ```

*Note: For creating a new application using Next.js, use `npx create-next-app@latest`.*

## Usage

### Development
To start the local development environment for the framework:
```bash
pnpm dev
```

### Running Tests
Next.js has a robust testing suite using Jest and a custom test runner. You can run tests using the `run-tests.js` script provided in the root:

```bash
# Run all tests
node run-tests.js

# Run tests with a specific pattern
node run-tests.js --test-pattern "app-router"

# Run tests using Turbopack
IS_TURBOPACK_TEST=true node run-tests.js
```

### Benchmarking
The repository includes a comprehensive `bench/` directory to track performance:
```bash
cd bench/app-router-server
pnpm install
pnpm run bench
```

## Project Structure

The repository is organized into several key areas:

-   `packages/`: Contains the core `next` package and internal helper packages (codemods, ESLint plugins, fonts).
-   `bench/`: Performance benchmarking suites for various scenarios (App Router, minimal server, etc.).
-   `test/`: Global integration and unit tests.
-   `turbo.json`: Configuration for [Turborepo](https://turbo.build/), managing the build pipeline.
-   `jest.config.js` / `jest.config.turbopack.js`: Test configurations for both Webpack and Turbopack environments.
-   `run-tests.js`: A specialized CLI tool for executing the massive test suite with support for retries and concurrency.
-   `release.js`: Internal automation script for managing version releases and changelogs.

## Contributing

We love seeing contributions from the community! 

1.  **Read the Guidelines:** Please review the `contributing.md` file for instructions on our development workflow.
2.  **Code of Conduct:** Ensure you follow our `CODE_OF_CONDUCT.md` to maintain a welcoming environment.
3.  **Pull Requests:** When submitting a PR, use descriptive titles as the `release.js` script automatically categorizes changes based on labels (e.g., `type: next` for Core Changes, `documentation` for Docs).
4.  **Formatting:** The project uses Prettier and ESLint. Ensure your code passes linting by running:
    ```bash
    pnpm lint
    ```

Next.js is [MIT Licensed](license.md).