// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SUPAVISOR_NATIVE.Tenants
{
    public static class GetTenant
    {
        public static Task<Outputs.Tenant> InvokeAsync(GetTenantArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<Outputs.Tenant>("supavisor-native:tenants:getTenant", args ?? new GetTenantArgs(), options.WithDefaults());

        public static Output<Outputs.Tenant> Invoke(GetTenantInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<Outputs.Tenant>("supavisor-native:tenants:getTenant", args ?? new GetTenantInvokeArgs(), options.WithDefaults());

        public static Output<Outputs.Tenant> Invoke(GetTenantInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<Outputs.Tenant>("supavisor-native:tenants:getTenant", args ?? new GetTenantInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTenantArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// External ID of the tenant
        /// </summary>
        [Input("externalId", required: true)]
        public string ExternalId { get; set; } = null!;

        public GetTenantArgs()
        {
        }
        public static new GetTenantArgs Empty => new GetTenantArgs();
    }

    public sealed class GetTenantInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// External ID of the tenant
        /// </summary>
        [Input("externalId", required: true)]
        public Input<string> ExternalId { get; set; } = null!;

        public GetTenantInvokeArgs()
        {
        }
        public static new GetTenantInvokeArgs Empty => new GetTenantInvokeArgs();
    }
}
