# Claude Code Plugin Marketplace Template

A template repository for creating custom plugin marketplaces for Claude Code. This template allows you to organize and distribute your own collections of commands, agents, and skills that extend Claude Code's capabilities.

## Purpose

This repository serves as a starting point for building your own Claude Code plugin marketplace. It demonstrates the proper structure and configuration needed to:

- Create a plugin marketplace with multiple plugins
- Organize plugins into logical groups
- Include sample implementations of commands, agents, and skills
- Distribute your plugins to users of Claude Code

## Structure

The template includes:

- `.claude-plugin/marketplace.json` - Marketplace configuration and metadata
- `plugins/` - Directory containing individual plugins
  - `sample-plugin/` - Example plugin demonstrating the structure
    - `.claude-plugin/plugin.json` - Plugin metadata
    - `commands/` - User-invocable commands (e.g., joke.md)
    - `agents/` - Specialized agents for specific tasks (e.g., top-five.md)
    - `skills/` - Skills with executable scripts (e.g., palindrome/)

## Getting Started

1. Clone this template repository
2. Update `.claude-plugin/marketplace.json` with your marketplace details
3. Modify or replace the sample plugin with your own plugins
4. Add your custom commands, agents, and skills
5. Distribute your marketplace to Claude Code users

## Example Components

The sample plugin includes:
- **joke** command - Tells jokes based on user-provided topics
- **top-five** agent - Creates top 5 lists and saves them to markdown files
- **palindrome** skill - Reverses words/phrases using a Python script