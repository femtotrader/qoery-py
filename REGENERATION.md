# Regeneration Guide

This document explains how to regenerate the SDK when the OpenAPI spec changes.

## When to Regenerate

Regenerate the auto-generated client (`qoery/`) when:
- The OpenAPI spec (`docs/openapi.yaml`) is updated
- New endpoints are added
- Request/response models change
- API version changes

## How to Regenerate

```bash
# 1. Ensure you have the latest OpenAPI spec
# (This is automatically synced via GitHub Actions workflow)

# 2. Regenerate the client
openapi-generator-cli generate \
  -i docs/openapi.yaml \
  -g python \
  -o . \
  --package-name qoery \
  --additional-properties=projectName=qoery-py,packageVersion=0.1.0,library=urllib3

# 3. Test the wrapper still works
python examples/simple_usage.py
```

## What Gets Regenerated

The following are **automatically regenerated** (and will be overwritten):
- `qoery/` - All auto-generated code
- `test/` - Auto-generated tests
- `docs/*.md` - Auto-generated documentation (except custom docs)
- `setup.py`, `requirements.txt`, etc.

The following are **protected** (won't be overwritten):
- `qoery_sdk/` - Our custom wrapper
- `examples/simple_usage.py` - Custom examples
- `README.md` - Custom documentation
- `COMPARISON.md` - Custom documentation
- `.github/workflows/` - Custom workflows

## Compatibility Considerations

### Breaking Changes

The wrapper (`qoery_sdk`) depends on the generated code (`qoery`). Breaking changes in the OpenAPI spec could break the wrapper if:

1. **Property names change** - e.g., `amount_usd` becomes `amountUSD`
2. **Required parameters added** - New mandatory fields in requests
3. **Response structure changes** - Nested objects become flat or vice versa

### Maintaining Compatibility

**Best practices:**

1. **Use API versioning** - The API uses `/v0` in the URL, new versions should be `/v1`, etc.
2. **Test after regeneration** - Always run examples after regenerating
3. **Semantic versioning** - Increment SDK version appropriately:
   - Patch (0.1.1): Bug fixes, no API changes
   - Minor (0.2.0): New features, backward compatible
   - Major (1.0.0): Breaking changes

### Handling Breaking Changes

If regeneration breaks the wrapper, update the adapter layer in `qoery_sdk/`:

**Example:** If property name changes from `amount_usd` to `amountUSD`:

```python
# In qoery_sdk/models.py
@dataclass
class Tick:
    # ...
    amount_usd: float
    
    @classmethod
    def from_api(cls, api_tick):
        return cls(
            # ...
            # Handle both old and new property names
            amount_usd=getattr(api_tick, 'amount_usd', None) or getattr(api_tick, 'amountUSD', None),
        )
```

## Testing After Regeneration

Run these commands to verify everything works:

```bash
# 1. Check imports
python -c "import qoery_sdk; print('OK')"

# 2. Run examples
python examples/simple_usage.py

# 3. Run tests (if you have them)
pytest

# 4. Check for import errors
python -c "from qoery_sdk import Client; print('OK')"
```

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'qoery'`

**Solution:** The auto-generated code wasn't created. Run regeneration command.

### Issue: `AttributeError: 'Candle' object has no attribute 'time'`

**Solution:** Property name changed in API. Update the wrapper's `from_api()` methods.

### Issue: Pydantic version errors

**Solution:** The generated code might require a specific Pydantic version. Check `requirements.txt`.

## Automation

The OpenAPI spec is automatically synced from the backend repo via GitHub Actions:
- `.github/workflows/sync-openapi.yml`
- Runs daily at midnight UTC
- Can be manually triggered

After the spec syncs, you may want to:
1. Regenerate the client
2. Test the wrapper
3. Update the wrapper if needed
4. Release a new SDK version
