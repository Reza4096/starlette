# Applications

<p>Starlette includes an application class <code>Starlette</code> that nicely ties together all of
its other functionality.</p>

## Instantiating the application

<div class="autodoc-signature"><em>class </em><code>starlette.applications.<strong>Starlette</strong></code><span class="autodoc-punctuation">(</span><em class="autodoc-param">debug=False</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">routes=None</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">middleware=None</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">exception_handlers=None</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">on_startup=None</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">on_shutdown=None</em><span class="autodoc-punctuation">, </span><em class="autodoc-param">lifespan=None</em><span class="autodoc-punctuation">)</span></div>

Creates an application instance.

## Parameters:

<ul>
<li><strong>debug</strong> - Boolean indicating if debug tracebacks should be returned on errors.</li>
<li><strong>routes</strong> - A list of routes to serve incoming HTTP and WebSocket requests.</li>
<li><strong>middleware</strong> - A list of middleware to run for every request. A starlette
application will always automatically include two middleware classes.
<code>ServerErrorMiddleware</code> is added as the very outermost middleware, to handle
any uncaught errors occurring anywhere in the entire stack.
<code>ExceptionMiddleware</code> is added as the very innermost middleware, to deal
with handled exception cases occurring in the routing or endpoints.</li>
<li><strong>exception_handlers</strong> - A mapping of either integer status codes,
or exception class types onto callables which handle the exceptions.
Exception handler callables should be of the form
<code>handler(request, exc) -&gt; response</code> and may be be either standard functions, or
async functions.</li>
<li><strong>on_startup</strong> - A list of callables to run on application startup.
Startup handler callables do not take any arguments, and may be be either
standard functions, or async functions.</li>
<li><strong>on_shutdown</strong> - A list of callables to run on application shutdown.
Shutdown handler callables do not take any arguments, and may be be either
standard functions, or async functions.</li>
</ul>

## Storing state on the app instance

<p>You can store arbitrary extra state on the application instance, using the
generic <code>app.state</code> attribute.</p>

For example:

```python
app.state.ADMIN_EMAIL = 'reza4096@yahoo.com'
```

## Accessing the app instance
<p>Where a <code>request</code> is available (i.e. endpoints and middleware), the app is available on <code>request.app</code>.</p>